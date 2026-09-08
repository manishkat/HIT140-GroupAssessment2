"""
FIFA World Cup 2026 - Possession vs Match Outcome
Task: Confidence Interval Estimation

Calculates a 95% confidence interval for the mean possession of each group
(winning teams and losing teams), estimating the true population mean
based on the sample data.
"""

import pandas as pd
import numpy as np
from scipy import stats

sample_winners = pd.read_csv('sample_winners.csv')['Possession%']
sample_losers = pd.read_csv('sample_losers.csv')['Possession%']

def confidence_interval(sample, confidence=0.95):
    n = len(sample)
    mean = sample.mean()
    sd = sample.std(ddof=1)
    se = sd / np.sqrt(n)  # standard error

    # t-distribution is used instead of z, since the population standard
    # deviation is unknown and is being estimated from the sample.
    t_crit = stats.t.ppf((1 + confidence) / 2, df=n - 1)
    margin = t_crit * se

    return mean, mean - margin, mean + margin

mean_win, lower_win, upper_win = confidence_interval(sample_winners)
mean_lose, lower_lose, upper_lose = confidence_interval(sample_losers)

print("95% Confidence Interval - Winning Teams")
print("  Sample mean: {:.2f}%".format(mean_win))
print("  CI: ({:.2f}%, {:.2f}%)".format(lower_win, upper_win))

print("\n95% Confidence Interval - Losing Teams")
print("  Sample mean: {:.2f}%".format(mean_lose))
print("  CI: ({:.2f}%, {:.2f}%)".format(lower_lose, upper_lose))