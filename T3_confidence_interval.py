# T3_confidence_interval.py
# S226_HIT140 - Group 76
# 95% CI for the difference in mean attempts_at_goal between UEFA and CAF.
# using Welch's version (not the pooled one) because the two groups
# have pretty different standard deviations - UEFA's is almost double CAF's
 


import pandas as pd
from scipy import stats

INPUT_FILE = "T3_Players_Stats.csv"
VARIABLE = "attempts_at_goal"
CONFIDENCE_LEVEL = 0.95


def main():
    df = pd.read_csv(INPUT_FILE)
    df = df[df["confederation"].isin(["UEFA", "CAF"])]

    uefa = df[df["confederation"] == "UEFA"][VARIABLE]
    caf = df[df["confederation"] == "CAF"][VARIABLE]

    n1, n2 = len(uefa), len(caf)
    m1, m2 = uefa.mean(), caf.mean()
    s1, s2 = uefa.std(ddof=1), caf.std(ddof=1)

    # Welch's standard error (unequal variances)
    se = (s1**2 / n1 + s2**2 / n2) ** 0.5

    # Welch-Satterthwaite degrees of freedom
    df_welch = (s1**2 / n1 + s2**2 / n2) ** 2 / (
        (s1**2 / n1) ** 2 / (n1 - 1) + (s2**2 / n2) ** 2 / (n2 - 1)
    )

    alpha = 1 - CONFIDENCE_LEVEL
    tcrit = stats.t.ppf(1 - alpha / 2, df_welch)

    diff = m1 - m2
    margin = tcrit * se
    ci = (diff - margin, diff + margin)

    print("=" * 60)
    print(f"{int(CONFIDENCE_LEVEL*100)}% CI for difference in means: "
          f"UEFA (n={n1}) vs CAF (n={n2})")
    print("=" * 60)
    print(f"Mean UEFA = {m1:.3f}, SD = {s1:.3f}")
    print(f"Mean CAF  = {m2:.3f}, SD = {s2:.3f}")
    print(f"Difference (UEFA - CAF) = {diff:.3f}")
    print(f"Standard error (Welch)  = {se:.3f}")
    print(f"Welch-Satterthwaite df  = {df_welch:.1f}")
    print(f"t critical (two-tailed) = {tcrit:.3f}")
    print(f"\n95% CI: ({ci[0]:.3f}, {ci[1]:.3f})")

    if ci[0] > 0 or ci[1] < 0:
        print("The interval does NOT contain 0 -> suggests a genuine "
              "difference in population means.")
    else:
        print("The interval DOES contain 0 -> no clear evidence of a "
              "difference in population means.")


if __name__ == "__main__":
    main()
