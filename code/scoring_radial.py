
import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = [
    "Modularity", "Testability", "Scalability", "Deployment", "Performance", "Complexity", "Tooling", "Reusability"
]

# Scores out of 10 for each pattern
scores = {
    "MVC":                      [ 7.0,   4.5,   3.6,   5.0,   7.2,   6.3,   4.0,   6.3],
    "MVP":                      [ 8.0,   7.2,   4.2,   7.0,   6.3,   4.9,   3.5,   7.2],
    "MVVM":                     [ 9.0,   8.1,   4.8,   9.0,   5.4,   4.2,   2.0,   3.6],
    "Hexagonal Architecture":   [10.0,   9.0,   6.0,  10.0,   4.5,   3.5,   4.5,   9.0],
    "Plugin System":            [ 9.0,   7.2,   5.4,   9.0,   5.4,   4.2,   4.5,   8.1],
    "Onion Architecture":       [10.0,   9.0,   6.0,  10.0,   4.5,   2.8,   3.5,   9.0],
    "Front Controller":         [ 5.0,   2.7,   2.4,   4.0,   6.3,   5.6,   3.0,   3.6],
    "Backend-for-Frontend":     [ 9.0,   7.2,   5.4,   8.0,   6.3,   4.2,   3.5,   5.4],
    "Model-View-Adapter":       [ 7.0,   5.4,   3.6,   6.0,   6.3,   4.9,   3.0,   6.3],
    "Microkernel Architecture": [ 9.0,   7.2,   5.4,  10.0,   8.1,   6.3,   3.0,   8.1]
}

# Calculate totals
totals = {pattern: sum(vals) for pattern, vals in scores.items()}

N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))

for pattern, vals in scores.items():
    vals_closed = vals + vals[:1]
    total = totals[pattern]

    ax.plot(angles, vals_closed, linewidth=2, label=f"{pattern} (Total: {total:.1f})")
    ax.fill(angles, vals_closed, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_ylim(0, 10)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
plt.title("Evaluation of Software Architecture Patterns", size=16, y=1.1)
plt.tight_layout()
plt.show()