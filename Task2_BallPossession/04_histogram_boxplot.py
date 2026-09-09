"""
FIFA World Cup 2026 - Possession vs Match Outcome
Task: Checking Statistical Assumptions

Before running a t-test, we visually check whether each sample is
roughly normally distributed and whether there are any outliers.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sample_winners = pd.read_csv('sample_winners.csv')['Possession%']
sample_losers = pd.read_csv('sample_losers.csv')['Possession%']

# Histograms - check the shape of each sample's distribution
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.histplot(sample_winners, kde=True, ax=axes[0])
axes[0].set_title('Winning Teams - Possession % Distribution')
axes[0].set_xlabel('Possession %')

sns.histplot(sample_losers, kde=True, ax=axes[1])
axes[1].set_title('Losing Teams - Possession % Distribution')
axes[1].set_xlabel('Possession %')

plt.tight_layout()
plt.savefig('histogram_possession.png')
plt.show()

# Boxplot - check for outliers in each group
# Build a proper two-column table so seaborn plots both groups side by side
boxplot_data = pd.DataFrame({
    'Winning Teams': sample_winners.reset_index(drop=True),
    'Losing Teams': sample_losers.reset_index(drop=True)
})

fig2, ax2 = plt.subplots(figsize=(6, 5))
sns.boxplot(data=boxplot_data)
ax2.set_ylabel('Possession %')
ax2.set_title('Possession % by Match Outcome')
plt.savefig('boxplot_possession.png')
plt.show()

print("Saved histogram_possession.png and boxplot_possession.png")