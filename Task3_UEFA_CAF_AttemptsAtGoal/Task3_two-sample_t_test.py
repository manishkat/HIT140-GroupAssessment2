
# Task3_two-sample_t_test.py
# S226_HIT140 - Group 76
# Welch's two-sample t-test comparing mean attempts at goal between
# UEFA and CAF players at the FIFA World Cup 2026.

# H0: mu_UEFA = mu_CAF   (no difference in mean attempts at goal)
# Ha: mu_UEFA != mu_CAF  (a difference exists) -- two-tailed test

# Input : Task3_Players_Stats_sampled.csv (random sample of 38 UEFA and
#         38 CAF players drawn from Task3_Players_Stats.csv, see Task3_sample.py)
# Output: prints the test statistic, degrees of freedom, p-value, and
#         the decision at alpha = 0.05


import pandas as pd
from scipy import stats

INPUT_FILE = "Task3_Players_Stats_sampled.csv"
VARIABLE = "attempts_at_goal"
ALPHA = 0.05


def main():
    df = pd.read_csv(INPUT_FILE)
    df = df[df["confederation"].isin(["UEFA", "CAF"])]

    uefa = df[df["confederation"] == "UEFA"][VARIABLE]
    caf = df[df["confederation"] == "CAF"][VARIABLE]

    # Welch's t-test: does NOT assume equal population variances,
    # appropriate here since UEFA's SD is noticeably larger than CAF's.
    t_stat, p_val = stats.ttest_ind(uefa, caf, equal_var=False)

    n1, n2 = len(uefa), len(caf)
    s1, s2 = uefa.std(ddof=1), caf.std(ddof=1)
    df_welch = (s1**2 / n1 + s2**2 / n2) ** 2 / (
        (s1**2 / n1) ** 2 / (n1 - 1) + (s2**2 / n2) ** 2 / (n2 - 1)
    )

    print("=" * 60)
    print("Welch's Two-Sample t-Test: attempts_at_goal, UEFA vs CAF")
    print("=" * 60)
    print("H0: mu_UEFA = mu_CAF")
    print("Ha: mu_UEFA != mu_CAF (two-tailed)")
    print(f"\nUEFA: n={n1}, mean={uefa.mean():.3f}, SD={s1:.3f}")
    print(f"CAF:  n={n2}, mean={caf.mean():.3f}, SD={s2:.3f}")
    print(f"\nt = {t_stat:.3f}, df = {df_welch:.1f}, p = {p_val:.4f}")

    if p_val < ALPHA:
        print(f"\nDecision at alpha = {ALPHA}: REJECT H0 -- statistically significant.")
        higher = "UEFA" if uefa.mean() > caf.mean() else "CAF"
        print(f"{higher} players recorded significantly more attempts "
              f"at goal on average.")
    else:
        print(f"\nDecision at alpha = {ALPHA}: FAIL TO REJECT H0 -- "
              f"not statistically significant.")


if __name__ == "__main__":
    main()
