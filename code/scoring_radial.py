
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

# ---------- Data ----------
categories = [
    "Separation", "Scalability", "Extensibility",
    "Deployment", "Performance", "Tooling"
]

scores = {
    "MVC":                      [  7,  5,  0,  5,  8,  8],
    "MVP":                      [  8,  8,  0,  7,  7,  7],
    "MVVM":                     [  9,  9,  0,  9,  6,  4],
    "MVA":                      [  7,  6,  0,  6,  7,  6],
    "Hexagonal":                [ 10, 10,  0,  8,  5,  9],
    "Onion":                    [ 10, 10,  0,  9,  5,  7],
    "Front Controller":         [  5,  3,  0,  4,  7,  6],
    "Backend-for-Frontend":     [  9,  8,  0,  8,  7,  7],
    "Microkernel":              [  9,  8,  0, 10, 10,  8]
}

score_weight = [1.00, 0.50, 0.50, 1.0, 1.00, 0.25]
N = len(categories)

# Compute weighted scores and totals
weighted_scores = {}
total_weighted = {}
for pattern, vals in scores.items():
    wvals = [vals[i] * score_weight[i] for i in range(N)]
    weighted_scores[pattern] = wvals
    total_weighted[pattern] = sum(wvals)

# Radar angles
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]   # close the loop

# ---------- 1. Combined overview figure (radar + bar) ----------
fig_overview = plt.figure(figsize=(14, 8))

# Left: radar (all patterns)
ax_radar = fig_overview.add_subplot(1, 2, 1, polar=True)
cmap = plt.cm.get_cmap('tab20', len(scores))
colors = {pattern: cmap(i) for i, pattern in enumerate(scores.keys())}
line_styles = ['-', '--', '-.', ':', (0, (1,1)), (0, (3,1,1,1))]

for idx, (pattern, vals) in enumerate(weighted_scores.items()):
    vals_closed = vals + vals[:1]
    color = colors[pattern]
    style = line_styles[idx % len(line_styles)]
    ax_radar.plot(angles, vals_closed, linewidth=2, label=pattern,
                  color=color, linestyle=style, marker='o', markersize=4)

ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(categories)
ax_radar.set_ylim(0, 10)
ax_radar.set_title("Weighted Category Scores\n(score x weight)", size=12, pad=20)
ax_radar.legend(loc='upper left', bbox_to_anchor=(1.1, 1.0), fontsize=8)

# Right: bar chart (total scores)
ax_bar = fig_overview.add_subplot(1, 2, 2)
sorted_patterns = sorted(total_weighted.items(), key=lambda x: x[1], reverse=True)
names = [p[0] for p in sorted_patterns]
totals_sorted = [p[1] for p in sorted_patterns]
bar_colors = [colors[name] for name in names]

bars = ax_bar.barh(names, totals_sorted, color=bar_colors)
ax_bar.set_xlabel('Total Weighted Score (max 50.5)')
ax_bar.set_title('Total Weighted Score Comparison')
ax_bar.invert_yaxis()
for bar, val in zip(bars, totals_sorted):
    ax_bar.text(val - 2, bar.get_y() + bar.get_height()/2, f'{val:.1f}',
                va='center', fontsize=11)

fig_overview.suptitle("Evaluation Overview (with category weights)", size=16, y=1.02)
plt.tight_layout()

# ---------- 2. Grid of individual radar plots (more horizontal space) ----------
n_patterns = len(weighted_scores)
n_cols = 3
n_rows = (n_patterns + n_cols - 1) // n_cols

# Increase figure width: 7 inches per column instead of 5
fig_grid, axes = plt.subplots(n_rows, n_cols, subplot_kw={'polar': True},
                              figsize=(7 * n_cols, 5 * n_rows))
# Add extra horizontal space between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.3)

axes = axes.flatten()

for ax, (pattern, wvals) in zip(axes, weighted_scores.items()):
    wvals_closed = wvals + wvals[:1]
    ax.plot(angles, wvals_closed, linewidth=2, color='steelblue', marker='o')
    ax.fill(angles, wvals_closed, alpha=0.2, color='steelblue')
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=8)   # slightly larger labels
    ax.set_ylim(0, 10)
    ax.set_title(pattern, fontsize=10, pad=10)

    total = total_weighted[pattern]
    ax.text(0, 0, f'Total: {total:.1f}', ha='center', va='center',
            fontsize=9, bbox=dict(facecolor='white', alpha=0.7, boxstyle='round'))

# Hide unused subplots
for i in range(len(weighted_scores), len(axes)):
    axes[i].set_visible(False)

fig_grid.suptitle("Individual Architecture Patterns – Weighted Scores", fontsize=14, y=1.02)

# ---------- 3. Command‑line argument: save individual plots as PNG ----------
def save_individual_radars():
    """Save each individual radar plot (from the grid) as a separate PNG file."""
    save_dir = Path(__file__).parent   # script's directory
    for pattern, wvals in weighted_scores.items():
        # Create a new figure for each pattern
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
        wvals_closed = wvals + wvals[:1]
        ax.plot(angles, wvals_closed, linewidth=2, color='steelblue', marker='o')
        ax.fill(angles, wvals_closed, alpha=0.2, color='steelblue')
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_ylim(0, 10)
        ax.set_title(f"{pattern}\nWeighted Category Scores", size=12, pad=20)
        ax.text(0, 0, f'Total: {total_weighted[pattern]:.1f}', ha='center', va='center',
                fontsize=12, bbox=dict(facecolor='white', alpha=0.8, boxstyle='round'))
        plt.tight_layout()
        filename = save_dir / f"{pattern.replace(' ', '_')}_radar.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f"Saved: {filename}")
    print("All individual radar plots saved.")

# Check command‑line arguments
if len(sys.argv) > 1 and sys.argv[1] in ('--save', '-s'):
    save_individual_radars()

# Show the figures (overview + grid)
plt.show()
