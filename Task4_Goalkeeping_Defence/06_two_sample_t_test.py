"""
Task 3 - Goalkeeping & Defensive Performance
Step 6: Inferential Statistics - Two-Sample t-Test

Step 1 (State):
Analytic question - On average, is there a statistically significant
difference in save percentage between goalkeepers whose team advanced to
the knockout stage and goalkeepers whose team was eliminated in the group
stage at the FIFA World Cup 2026?

Step 2 (Plan):
Two-sided, independent two-sample t-test.
    H0: mu_advanced = mu_eliminated  (no difference in mean save %)
    Ha: mu_advanced != mu_eliminated (a difference in mean save % exists)

Welch's t-test (unequal-variance) is used rather than a pooled-variance
test because the two groups have unequal sample sizes (22 vs 11) and
unequal variances (SD 12.49 vs 13.36) - eliminated teams only ever played
3 group-stage games, so their save % estimate carries more sampling
variability than advanced teams' figures.
"""

import os
import pandas as pd
from scipy import stats

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("fifa_SAMPLE_savepct_n33.csv")

adv = df.loc[df["advanced"] == True, "save_pct"]
elim = df.loc[df["advanced"] == False, "save_pct"]

print("Step 3: Solve\n")
print(f"{'Statistic':22s}{'Advanced':>12s}{'Eliminated':>14s}")
print(f"{'Sample Size':22s}{len(adv):12d}{len(elim):14d}")
print(f"{'Mean':22s}{adv.mean():12.2f}{elim.mean():14.2f}")
print(f"{'Standard Deviation':22s}{adv.std(ddof=1):12.2f}{elim.std(ddof=1):14.2f}")

t_stat, p_value = stats.ttest_ind(adv, elim, equal_var=False)
alpha = 0.05

print("\nWelch two-sample t-test result")
print(f"  t-statistic (t*)        : {t_stat:.3f}")
print(f"  p-value                 : {p_value:.3f}")
print(f"  Significance level (a)  : {alpha}")
decision = "Reject H0" if p_value < alpha else "Fail to reject H0"
print(f"  Decision                : {decision}")

print("\nStep 4: Conclude")
if p_value < alpha:
    print(f"Since the p-value ({p_value:.3f}) is less than {alpha}, the null hypothesis is "
          "rejected. There is statistically significant evidence that goalkeepers on teams "
          "that advanced to the knockout stage have a different average save percentage than "
          "goalkeepers on teams eliminated in the group stage.")
    higher = "Advanced" if adv.mean() > elim.mean() else "Eliminated"
    print(f"{higher} teams recorded the higher sample mean save % "
          f"({max(adv.mean(), elim.mean()):.2f} vs {min(adv.mean(), elim.mean()):.2f}).")
else:
    print(f"Since the p-value ({p_value:.3f}) is greater than or equal to {alpha}, the null "
          "hypothesis is not rejected.")
