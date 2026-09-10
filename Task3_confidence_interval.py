# Task3_confidence_interval.py
# S226_HIT140 - Group 76
# 95% confidence intervals for mean attempts at goal
# for UEFA and CAF players, plus the 95% CI for the
# difference in means (UEFA - CAF) using Welch's method.

# Input : Task3_Players_Stats_sampled.csv
#         random sample of 38 UEFA and 38 CAF players

import pandas as pd
from scipy import stats
import math

INPUT_FILE = "Task3_Players_Stats_sampled.csv"
VARIABLE = "attempts_at_goal"
CONFIDENCE_LEVEL = 0.95


def confidence_interval(sample):

    # sample statistics
    mean = sample.mean()
    sd = sample.std(ddof=1)
    n = len(sample)

    # standard error
    se = sd / math.sqrt(n)

    # degrees of freedom
    df = n - 1

    # significance level
    alpha = 1 - CONFIDENCE_LEVEL

    # t critical value
    t_crit = stats.t.ppf(1 - alpha / 2, df)

    # margin of error
    margin = t_crit * se

    # lower and upper confidence limits
    lower = mean - margin
    upper = mean + margin

    return mean, sd, n, se, df, t_crit, lower, upper


def difference_confidence_interval(sample1, sample2):

    # sample statistics
    mean1, mean2 = sample1.mean(), sample2.mean()
    sd1, sd2 = sample1.std(ddof=1), sample2.std(ddof=1)
    n1, n2 = len(sample1), len(sample2)

    # Welch's standard error (unequal variances)
    se = math.sqrt(sd1**2 / n1 + sd2**2 / n2)

    # Welch-Satterthwaite degrees of freedom
    df = (sd1**2 / n1 + sd2**2 / n2) ** 2 / (
        (sd1**2 / n1) ** 2 / (n1 - 1) + (sd2**2 / n2) ** 2 / (n2 - 1)
    )

    # significance level
    alpha = 1 - CONFIDENCE_LEVEL

    # t critical value
    t_crit = stats.t.ppf(1 - alpha / 2, df)

    # difference and margin of error
    diff = mean1 - mean2
    margin = t_crit * se

    # lower and upper confidence limits
    lower = diff - margin
    upper = diff + margin

    return diff, se, df, t_crit, lower, upper


def main():

    data = pd.read_csv(INPUT_FILE)

    # keep only UEFA and CAF
    data = data[data["confederation"].isin(["UEFA", "CAF"])]

    # separate samples
    uefa = data[data["confederation"] == "UEFA"][VARIABLE]
    caf = data[data["confederation"] == "CAF"][VARIABLE]

    # UEFA confidence interval
    mean, sd, n, se, df, t_crit, lower, upper = confidence_interval(uefa)

    print("=" * 60)
    print("UEFA - 95% Confidence Interval")
    print("=" * 60)
    print("Mean: %.2f" % mean)
    print("Standard deviation: %.2f" % sd)
    print("Sample size: %d" % n)
    print("Standard error: %.2f" % se)
    print("Degrees of freedom: %d" % df)
    print("t critical: %.3f" % t_crit)
    print("95%% Confidence Interval: %.2f to %.2f" % (lower, upper))

    # CAF confidence interval
    mean, sd, n, se, df, t_crit, lower, upper = confidence_interval(caf)

    print("\n" + "=" * 60)
    print("CAF - 95% Confidence Interval")
    print("=" * 60)
    print("Mean: %.2f" % mean)
    print("Standard deviation: %.2f" % sd)
    print("Sample size: %d" % n)
    print("Standard error: %.2f" % se)
    print("Degrees of freedom: %d" % df)
    print("t critical: %.3f" % t_crit)
    print("95%% Confidence Interval: %.2f to %.2f" % (lower, upper))

    # Difference in means (UEFA - CAF), Welch's method
    diff, se, df, t_crit, lower, upper = difference_confidence_interval(uefa, caf)

    print("\n" + "=" * 60)
    print("Difference in Means (UEFA - CAF) - 95% Confidence Interval")
    print("=" * 60)
    print("Difference: %.2f" % diff)
    print("Standard error (Welch): %.2f" % se)
    print("Welch-Satterthwaite degrees of freedom: %.1f" % df)
    print("t critical: %.3f" % t_crit)
    print("95%% Confidence Interval: %.2f to %.2f" % (lower, upper))

    if lower > 0 or upper < 0:
        print("The interval does NOT contain 0 -> suggests a genuine "
              "difference in population means.")
    else:
        print("The interval DOES contain 0 -> no clear evidence of a "
              "difference in population means.")


if __name__ == "__main__":
    main()