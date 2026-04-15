#!/usr/bin/env python3
"""
Interactive BibTeX entry creator from websites and citation‑key resolver.
- Paste a URL → adds an @online entry to your .bib file.
- Paste citation keys like [@smith2023example] [@jones2022test] → shows URLs.
Exit with 'q' or Ctrl+C.
Dependencies: requests, beautifulsoup4
Optional: cloudscraper (for Cloudflare/403 bypass)
Install: pip install requests beautifulsoup4 cloudscraper
"""

import re
import json
import sys
from datetime import datetime
from urllib.parse import urlparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Try to import cloudscraper for stubborn sites
try:
    import cloudscraper
    HAS_CLOUDSCRAPER = True
except ImportError:
    HAS_CLOUDSCRAPER = False


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

    # Fallback: use domain name
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
    Braces { } and backslashes \\ are left untouched.
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
    title_esc = escape_bibtex(title)
    author_esc = escape_bibtex(author)
    year = date[:4] if len(date) >= 4 and date[:4].isdigit() else "n.d."

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


def get_soup_with_fallback(url):
    """
    Attempt to fetch and parse a URL using multiple strategies.
    Returns (soup, success_flag) or (None, False) on complete failure.
    """
    # Enhanced browser headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
    }

    # Try normal requests with session
    session = requests.Session()
    session.headers.update(headers)
    try:
        resp = session.get(url, timeout=15)
        resp.raise_for_status()
        return BeautifulSoup(resp.text, 'html.parser'), True
    except requests.exceptions.RequestException as e:
        print(f"Standard request failed: {e}")

    # If 403 and cloudscraper is available, try that
    if HAS_CLOUDSCRAPER:
        print("Trying cloudscraper to bypass bot protection...")
        try:
            scraper = cloudscraper.create_scraper()
            resp = scraper.get(url, timeout=20)
            resp.raise_for_status()
            return BeautifulSoup(resp.text, 'html.parser'), True
        except Exception as e:
            print(f"cloudscraper also failed: {e}")

    # Special handling for Medium (use JSON API if possible)
    if "medium.com" in url:
        print("Medium detected – trying alternative API endpoint...")
        # Convert article URL to JSON format: https://medium.com/@user/post -> https://medium.com/@user/post?format=json
        json_url = url + "?format=json"
        try:
            resp = session.get(json_url, timeout=10)
            # Medium wraps JSON in "])}while(1);</x>" – strip it
            if resp.status_code == 200:
                raw = resp.text
                # Remove the garbage prefix
                if raw.startswith("])}while(1);</x>"):
                    raw = raw.split("</x>", 1)[-1]
                data = json.loads(raw)
                # Extract title and author from the payload
                title = data.get("payload", {}).get("title") or data.get("title")
                author = data.get("payload", {}).get("author", {}).get("name") or data.get("author")
                date = data.get("payload", {}).get("publishedAt", "")[:10] or ""
                # Manually build a minimal soup with these fields
                class FakeSoup:
                    pass
                soup = FakeSoup()
                soup.title = lambda: None
                soup.title.string = title
                # For author/date extraction we'll just return special values
                # We'll handle this outside the soup mechanism
                return (soup, True, {"title": title, "author": author, "date": date})
        except Exception as e:
            print(f"Medium API attempt failed: {e}")

    return None, False


def add_url_to_bib(bib_path, url, force=False):
    """Fetch, create entry, and append to bib file if not duplicate (or force)."""
    if not force and is_url_in_bibfile(bib_path, url):
        print(f"URL already exists in {bib_path.name}. Skipping.")
        return False

    # Attempt to fetch soup
    result = get_soup_with_fallback(url)
    if len(result) == 3:  # Medium API special case
        soup, success, extra = result
        if success:
            title = extra.get("title", extract_title(soup, url))
            author = extra.get("author", extract_author(soup, url))
            date = extra.get("date", extract_date(soup))
        else:
            title = author = date = None
    else:
        soup, success = result
        if success:
            title = extract_title(soup, url)
            author = extract_author(soup, url)
            date = extract_date(soup)
        else:
            title = author = date = None

    # If all automatic methods failed, ask for manual input
    if not success or not title:
        print("\n⚠️  Could not fetch page automatically (403 or other error).")
        print("Please provide the following information manually:")
        title = input("  Title: ").strip()
        if not title:
            title = urlparse(url).netloc
        author = input("  Author (or domain): ").strip()
        if not author:
            author = urlparse(url).netloc
        date = input("  Date (YYYY-MM-DD or n.d.): ").strip()
        if not date:
            date = "n.d."

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


def parse_bib_for_urls(bib_path):
    """
    Read a .bib file and return a dict mapping citation keys to URLs.
    Only looks at @online entries.
    """
    key_to_url = {}
    if not bib_path.exists():
        return key_to_url

    content = bib_path.read_text(encoding='utf-8')
    # Split on lines that start with @online (simplistic, but works for our own format)
    entries = re.split(r'\n(?=@online\{)', content)
    for entry in entries:
        # Extract key: @online{key,
        key_match = re.search(r'@online\{([^,]+),', entry)
        if not key_match:
            continue
        key = key_match.group(1).strip()
        # Extract URL
        url_match = re.search(r'url\s*=\s*[{"\']([^"\'}]+)[}"\']', entry, re.IGNORECASE)
        if url_match:
            url = url_match.group(1).strip()
            key_to_url[key] = url
    return key_to_url


def handle_citation_lookup(bib_path, input_text):
    """
    Detect citation keys like [@key1] [@key2] and print their URLs.
    Returns True if input was a citation list and handled, else False.
    """
    # Look for patterns like [@somekey] - may be multiple separated by spaces
    pattern = r'\[@([^\]]+)\]'
    matches = re.findall(pattern, input_text)
    if not matches:
        return False

    # We found citation keys – handle them
    key_to_url = parse_bib_for_urls(bib_path)
    found_all = True
    urls = []

    for key in matches:
        url = key_to_url.get(key)
        if url:
            urls.append(url)
        else:
            print(f"⚠️  Citation key '@{key}' not found in {bib_path.name}")
            found_all = False

    if found_all:
        print("✅ All citation keys found.")
    else:
        print("❌ Some citation keys were not found.")

    if urls:
        print("\nLinks:")
        for url in urls:
            print(f"- {url}")
    else:
        print("No URLs to display.")

    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Interactive BibTeX entry creator from websites and citation lookup.")
    parser.add_argument("-o", "--output", default="references.bib", help="Output .bib file (default: references.bib)")
    args = parser.parse_args()

    bib_path = Path(args.output)
    print(f"BibTeX file: {bib_path}")
    if not HAS_CLOUDSCRAPER:
        print("Note: cloudscraper not installed. Install it for better 403 bypass: pip install cloudscraper")
    print("Enter URLs one per line to add them to the .bib file.")
    print("Paste citation keys like [@smith2023] [@jones2022] to look up their URLs.")
    print("Type 'q' or press Ctrl+C to quit.\n")

    while True:
        try:
            user_input = input("Input: ").strip()
            if user_input.lower() in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break
            if not user_input:
                continue

            # First, check if it looks like a citation key list
            if handle_citation_lookup(bib_path, user_input):
                continue

            # Otherwise treat as a URL to add
            add_url_to_bib(bib_path, user_input)

        except KeyboardInterrupt:
            print("\n\nExiting. Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()