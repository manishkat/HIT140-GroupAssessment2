"""
FIFA World Cup 2026 - Possession vs Match Outcome
Task: Two-Sample t-Test (Inferential Statistics)

Tests whether there is a statistically significant difference in average
ball possession % between winning teams and losing teams, using Welch's
two-sample t-test (which does not assume equal variances between groups).
"""

import pandas as pd
from scipy import stats

sample_winners = pd.read_csv('sample_winners.csv')['Possession%']
sample_losers = pd.read_csv('sample_losers.csv')['Possession%']

# Step 1: State
# Do winning and losing teams differ in average ball possession % at the
# FIFA World Cup 2026?

# Step 2: Plan
# H0: mu1 = mu2  (no difference in mean possession between winners and losers)
# Ha: mu1 != mu2 (there is a difference)
# Two-tailed test, since there is no prior assumption about direction.

# Step 3: Solve
# equal_var=False runs Welch's t-test, which does not assume the two
# groups have equal variances - appropriate here since we have not
# verified that assumption.
t_stat, p_value = stats.ttest_ind(sample_winners, sample_losers, equal_var=False)

print("Two-Sample t-Test (Welch's)")
print("t* = {:.2f}".format(t_stat))
print("p-value = {:.10f}".format(p_value))
print("p-value (scientific notation) = {:.4e}".format(p_value))

# Step 4: Conclude
alpha = 0.05
print("\nConclusion:")
if p_value <= alpha:
    print("p-value ({:.10f}) <= 0.05, so we reject the null hypothesis.".format(p_value))
    print("There is statistically significant evidence that winning and")
    print("losing teams differ in average ball possession.")
else:
    print("p-value ({:.10f}) > 0.05, so we fail to reject the null hypothesis.".format(p_value))
    print("There is not enough evidence that winning and losing teams")
    print("differ in average ball possession.")