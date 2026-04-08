
import matplotlib.pyplot as plt
import numpy as np

# Categories and scores (same as original)
categories = [
    "Separation", "Testability", "Scalability", "Deployment",
    "Performance",
    # "Complexity",
    "Tooling", "Reusability"
]

scores = {
    "MVC":                      [ 7.00,  4.50,  3.60,  5.00,  7.20,  4.00,  6.30],
    "MVP":                      [ 8.00,  7.20,  4.20,  7.00,  6.30,  3.50,  7.20],
    "MVVM":                     [ 9.00,  8.10,  4.80,  9.00,  5.40,  2.00,  3.60],
    "Hexagonal Architecture":   [10.00,  9.00,  6.00, 10.00,  4.50,  4.50,  9.00],
    "Onion Architecture":       [ 9.00,  8.55,  4.80,  8.00,  6.00,  3.50,  7.20],
    "Front Controller":         [ 5.00,  2.70,  2.40,  4.00,  6.30,  3.00,  3.60],
    "Backend-for-Frontend":     [ 9.00,  7.20,  5.40,  8.00,  6.30,  3.50,  5.40],
    "Model-View-Adapter":       [ 7.00,  5.40,  3.60,  6.00,  6.30,  3.00,  6.30],
    "Microkernel Architecture": [ 9.00,  7.20,  5.40, 10.00,  8.10,  4.00,  8.10]
}

# Calculate total scores
totals = {pattern: sum(vals) for pattern, vals in scores.items()}

# --- Define a consistent color map for all patterns ---
# Use a qualitative colormap with enough distinct colors
cmap = plt.cm.get_cmap('tab10', len(scores))
colors = {pattern: cmap(i) for i, pattern in enumerate(scores.keys())}

# Prepare radar chart data
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]   # close the loop

# Create figure with two subplots
fig = plt.figure(figsize=(14, 8))

# ---- Radar plot (left side) ----
ax_radar = fig.add_subplot(1, 2, 1, polar=True)
for pattern, vals in scores.items():
    vals_closed = vals + vals[:1]
    color = colors[pattern]
    ax_radar.plot(angles, vals_closed, linewidth=2, label=pattern, color=color)
    ax_radar.fill(angles, vals_closed, alpha=0.1, color=color)

ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(categories)
ax_radar.set_ylim(0, 10)
ax_radar.set_title("Radar Chart: Category Scores", size=12, pad=20)
# Place legend outside the radar plot to avoid clutter
ax_radar.legend(loc='upper left', bbox_to_anchor=(1.1, 1.0))

# ---- Bar chart (right side) ----
ax_bar = fig.add_subplot(1, 2, 2)
# Sort patterns by total score descending
sorted_patterns = sorted(totals.items(), key=lambda x: x[1], reverse=True)
names = [p[0] for p in sorted_patterns]
totals_sorted = [p[1] for p in sorted_patterns]
# Get the color for each pattern in the sorted order
bar_colors = [colors[name] for name in names]

bars = ax_bar.barh(names, totals_sorted, color=bar_colors)
ax_bar.set_xlabel('Total Score (sum of 8 weighted categories, max 65.5)')
ax_bar.set_title('Total Score Comparison')
ax_bar.invert_yaxis()   # highest at top
# Add value labels on bars
for bar, val in zip(bars, totals_sorted):
    bar.set_height(0.6)
    ax_bar.text(val - 5, bar.get_y() + bar.get_height()/2, f'{val:.1f}',
                va='center', fontsize=11)

plt.tight_layout()
plt.suptitle("Evaluation of Software Architecture Patterns", size=16, y=1.02)
plt.show()
