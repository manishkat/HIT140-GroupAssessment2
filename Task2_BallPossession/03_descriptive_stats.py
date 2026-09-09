"""
FIFA World Cup 2026 - Possession vs Match Outcome
Task: Descriptive Statistics

Loads the two random samples (winners and losers, n=40 each) and computes
descriptive statistics: mean, standard deviation, and range for each group.
"""

import pandas as pd
import numpy as np

sample_winners = pd.read_csv('sample_winners.csv')['Possession%']
sample_losers = pd.read_csv('sample_losers.csv')['Possession%']

# Sample mean and sample standard deviation (ddof=1 divides by n-1,
# which is the correct formula for a sample rather than a population).
mean_win = sample_winners.mean()
sd_win = sample_winners.std(ddof=1)
n_win = len(sample_winners)

mean_lose = sample_losers.mean()
sd_lose = sample_losers.std(ddof=1)
n_lose = len(sample_losers)

print("Winning teams (n = {}):".format(n_win))
print("  Mean possession: {:.2f}%".format(mean_win))
print("  Standard deviation: {:.2f}".format(sd_win))
print("  Min: {}, Max: {}".format(sample_winners.min(), sample_winners.max()))

print("\nLosing teams (n = {}):".format(n_lose))
print("  Mean possession: {:.2f}%".format(mean_lose))
print("  Standard deviation: {:.2f}".format(sd_lose))
print("  Min: {}, Max: {}".format(sample_losers.min(), sample_losers.max()))

print("\nDifference in means: {:.2f} percentage points".format(mean_win - mean_lose))