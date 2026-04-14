#!/usr/bin/env python3
"""
Interactive BibTeX entry creator from websites.
Continuously prompts for URLs and appends @online entries to a .bib file,
avoiding duplicates. Exit with 'q' or Ctrl+C.
Dependencies: requests, beautifulsoup4
Install: pip install requests beautifulsoup4
"""

import re
import json
import sys
from datetime import datetime
from urllib.parse import urlparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def clean_text(text):
    """Remove extra whitespace and normalize string."""
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()


def extract_title(soup, url):
    """Extract title from meta tags or <title>."""
    for prop in ['og:title', 'twitter:title']:
        meta = soup.find('meta', attrs={'property': prop}) or soup.find('meta', attrs={'name': prop})
        if meta and meta.get('content'):
            return clean_text(meta['content'])
    if soup.title and soup.title.string:
        return clean_text(soup.title.string)
    return urlparse(url).netloc


def extract_author(soup, url):
    """Try to find author from meta tags or JSON-LD."""
    for name in ['author', 'citation_author', 'article:author', 'dc.creator']:
        meta = soup.find('meta', attrs={'name': name}) or soup.find('meta', attrs={'property': name})
        if meta and meta.get('content'):
            return clean_text(meta['content'])

    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string)
            if isinstance(data, list):
                data = data[0] if data else {}
            if 'author' in data:
                author = data['author']
                if isinstance(author, dict) and 'name' in author:
                    return clean_text(author['name'])
                elif isinstance(author, str):
                    return clean_text(author)
        except (json.JSONDecodeError, TypeError, KeyError):
            continue

    # Fallback: use domain name without extra braces
    domain = urlparse(url).netloc.replace('www.', '')
    return domain


def extract_date(soup):
    """Extract publication date from meta tags or time elements."""
    for name in ['date', 'pubdate', 'article:published_time', 'citation_publication_date']:
        meta = soup.find('meta', attrs={'name': name}) or soup.find('meta', attrs={'property': name})
        if meta and meta.get('content'):
            return clean_text(meta['content'][:10])

    time_tag = soup.find('time')
    if time_tag and time_tag.get('datetime'):
        return clean_text(time_tag['datetime'][:10])
    if time_tag and time_tag.string:
        return clean_text(time_tag.string)

    return "n.d."


def generate_bibkey(author, year, title):
    """
    Create a clean BibTeX key like 'smith2023example'.
    Uses raw (unescaped) strings, strips non‑alphanumeric characters.
    """
    # Extract last part of author (surname)
    if author and author != "unknown":
        # Remove any punctuation, split by whitespace
        author_clean = re.sub(r'[^\w\s]', '', author)
        parts = author_clean.split()
        last = parts[-1].lower() if parts else 'unknown'
    else:
        last = 'unknown'

    # Year: take first 4 digits, or 'nodate'
    year_match = re.search(r'\b(19|20)\d{2}\b', year)
    year_clean = year_match.group(0) if year_match else 'nodate'

    # Title: first meaningful word (skip common stopwords), max 8 chars
    title_clean = re.sub(r'[^\w\s]', '', title.lower())
    words = title_clean.split()
    stopwords = {'the', 'a', 'an', 'and', 'of', 'to', 'in', 'for', 'on', 'with'}
    first_word = next((w for w in words if w not in stopwords), words[0] if words else 'webpage')
    key_word = first_word[:8]

    return f"{last}{year_clean}{key_word}"


def escape_bibtex(text):
    """
    Escape only characters that are truly special in BibTeX:
    & % $ # _ ~ ^
    Braces { } and backslashes \ are left untouched.
    """
    if not text:
        return ""
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    for char, repl in replacements.items():
        text = text.replace(char, repl)
    return text


def create_bibtex_entry(url, title, author, date, urldate):
    """Return a formatted BibTeX @online entry."""
    # Escape only special characters, not braces
    title_esc = escape_bibtex(title)
    author_esc = escape_bibtex(author)
    year = date[:4] if len(date) >= 4 and date[:4].isdigit() else "n.d."

    # Generate key from raw (unescaped) strings
    bibkey = generate_bibkey(author, year, title)

    return f"""@online{{{bibkey},
    title = {{{title_esc}}},
    author = {{{author_esc}}},
    url = {{{url}}},
    year = {{{year}}},
    date = {{{date}}},
    urldate = {{{urldate}}},
}}"""


def is_url_in_bibfile(bib_path, target_url):
    """Check if a URL already exists in the .bib file."""
    if not bib_path.exists():
        return False

    content = bib_path.read_text(encoding='utf-8')
    target_norm = target_url.rstrip('/')
    entries = re.split(r'\n(?=@online\{)', content)
    for entry in entries:
        match = re.search(r'url\s*=\s*[{"\']([^"\'}]+)[}"\']', entry, re.IGNORECASE)
        if match:
            existing_url = match.group(1).strip().rstrip('/')
            if existing_url == target_norm:
                return True
    return False


def add_url_to_bib(bib_path, url, force=False):
    """Fetch, create entry, and append to bib file if not duplicate (or force)."""
    if not force and is_url_in_bibfile(bib_path, url):
        print(f"URL already exists in {bib_path.name}. Skipping.")
        return False

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return False

    title = extract_title(soup, url)
    author = extract_author(soup, url)
    date = extract_date(soup)
    urldate = datetime.now().strftime("%Y-%m-%d")

    entry = create_bibtex_entry(url, title, author, date, urldate)

    # Write to file
    mode = 'a' if bib_path.exists() else 'w'
    with open(bib_path, mode, encoding='utf-8') as f:
        if mode == 'a' and bib_path.stat().st_size > 0:
            f.write("\n" + entry + "\n")
        else:
            f.write(entry + "\n")

    print(f"Added: {title[:60]}... -> {bib_path.name}")
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Interactive BibTeX entry creator from websites.")
    parser.add_argument("-o", "--output", default="references.bib", help="Output .bib file (default: references.bib)")
    args = parser.parse_args()

    bib_path = Path(args.output)
    print(f"BibTeX file: {bib_path}")
    print("Enter URLs one per line. Type 'q' or press Ctrl+C to quit.\n")

    while True:
        try:
            url = input("URL: ").strip()
            if url.lower() in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break
            if not url:
                continue
            add_url_to_bib(bib_path, url)
        except KeyboardInterrupt:
            print("\n\nExiting. Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()