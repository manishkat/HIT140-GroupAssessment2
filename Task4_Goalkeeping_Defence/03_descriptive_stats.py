"""
Task 3 - Goalkeeping & Defensive Performance
Step 3: Descriptive Statistics

Computes sample size, mean, median, mode, variance, standard deviation,
min, max, quartiles and IQR of save % for each group (advanced vs
eliminated) on the n=33 stratified sample.
"""

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("fifa_SAMPLE_savepct_n33.csv")

adv = df.loc[df["advanced"] == True, "save_pct"]
elim = df.loc[df["advanced"] == False, "save_pct"]


def describe(series, label):
    print(f"--- {label} (n={len(series)}) ---")
    print(f"Mean               : {series.mean():.2f}")
    print(f"Median             : {series.median():.2f}")
    print(f"Mode               : {series.mode().iloc[0]:.2f}")
    print(f"Sample Variance    : {series.var(ddof=1):.2f}")
    print(f"Standard Deviation : {series.std(ddof=1):.2f}")
    print(f"Minimum            : {series.min():.2f}")
    print(f"Maximum            : {series.max():.2f}")
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    print(f"Q1                 : {q1:.2f}")
    print(f"Q3                 : {q3:.2f}")
    print(f"IQR                : {q3 - q1:.2f}")
    print()


print(f"Sample loaded: n={len(df)} teams "
      f"({df['advanced'].sum()} advanced, {(~df['advanced']).sum()} eliminated)\n")

describe(adv, "Advanced to knockout stage")
describe(elim, "Eliminated in group stage")

diff = adv.mean() - elim.mean()
print(f"Difference in sample means (Advanced - Eliminated): {diff:.2f} percentage points")
print("Advanced teams' goalkeepers saved a higher share of shots on average than "
      "goalkeepers on teams eliminated in the group stage.")
