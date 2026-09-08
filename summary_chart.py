"""
FIFA World Cup 2026 - Possession vs Match Outcome
Task: Summary Visualization

A bar chart comparing mean possession % for winning vs losing teams,
with 95% confidence interval error bars, to visually summarise the
t-test result.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sample_winners = pd.read_csv('sample_winners.csv')['Possession%']
sample_losers = pd.read_csv('sample_losers.csv')['Possession%']

def mean_and_margin(sample, confidence=0.95):
    n = len(sample)
    mean = sample.mean()
    se = sample.std(ddof=1) / np.sqrt(n)
    t_crit = stats.t.ppf((1 + confidence) / 2, df=n - 1)
    return mean, t_crit * se

mean_win, margin_win = mean_and_margin(sample_winners)
mean_lose, margin_lose = mean_and_margin(sample_losers)

groups = ['Winning Teams', 'Losing Teams']
means = [mean_win, mean_lose]
errors = [margin_win, margin_lose]

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(groups, means, yerr=errors, capsize=8, color=['#4C72B0', '#DD8452'])
ax.set_ylabel('Mean Possession %')
ax.set_title('Mean Possession % by Match Outcome (with 95% CI)')

# Label each bar with its mean value
for bar, mean in zip(bars, means):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f'{mean:.1f}%', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('summary_bar_chart.png')
plt.show()

print("Saved summary_bar_chart.png")