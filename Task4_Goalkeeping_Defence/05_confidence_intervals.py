"""
Task 3 - Goalkeeping & Defensive Performance
Step 5: Inferential Statistics - 95% Confidence Interval

Estimates a 95% confidence interval for the mean save % across the n=33
sample, and for each group separately.
"""

import os
import pandas as pd
from scipy import stats

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("fifa_SAMPLE_savepct_n33.csv")

adv = df.loc[df["advanced"] == True, "save_pct"]
elim = df.loc[df["advanced"] == False, "save_pct"]
overall = df["save_pct"]


def ci95(series, label):
    mean = series.mean()
    sem = stats.sem(series)
    lo, hi = stats.t.interval(0.95, len(series) - 1, loc=mean, scale=sem)
    print(f"{label:28s} mean={mean:6.2f}  95% CI=({lo:.2f}, {hi:.2f})  width={hi - lo:.2f}")
    return lo, hi


print("95% Confidence Intervals for mean save %\n")
ci95(overall, "Sample overall (n=33)")
ci95(adv, "Advanced (n=22)")
ci95(elim, "Eliminated (n=11)")

print("\nInterpretation: we are 95% confident the true mean save percentage across "
      "all World Cup 2026 teams like these falls within the reported interval.")
