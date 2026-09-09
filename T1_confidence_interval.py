import scipy.stats as st
import statsmodels.stats.weightstats as stm
import pandas as pd
import math

# read csv
data = pd.read_csv("Players Stats.csv")

# keep players who played at least 90 minutes
data = data[data["Minutes Played"] >= 90]

# separate MF and DF populations
mf_population = data[data["Position"] == "MF"]
df_population = data[data["Position"] == "DF"]

# same random samples used in descriptive statistics
mf_sample = mf_population.sample(n=115, random_state=42)
df_sample = df_population.sample(n=115, random_state=42)


#MIDFIELDERS

sample = mf_sample["Completed passes / 90"].to_numpy()

# sample mean, standard deviation, and sample size
x_bar = st.tmean(sample)
s = st.tstd(sample)
n = len(sample)

print("MIDFIELDERS (MF)")
print("Mean: %.2f. Standard deviation: %.2f. Size: %d." %
      (x_bar, s, n))

# standard error
std_err = s / math.sqrt(n)
print("Standard error: %.2f" % std_err)

# confidence level, significance level, and degrees of freedom
conf_lvl = 0.95
sig_lvl = 1 - conf_lvl
df = n - 1

print("Degrees of freedom: %d" % df)
print("Confidence level: %.2f" % conf_lvl)
print("Significance level: %.2f" % sig_lvl)

# confidence interval with t-distribution
ci_low_t, ci_upp_t = stm._tconfint_generic(
    x_bar,
    std_err,
    df,
    alpha=sig_lvl,
    alternative="two-sided"
)

print("C.I. (t*): %.2f to %.2f. Interval size: %.2f." %
      (ci_low_t, ci_upp_t, ci_upp_t-ci_low_t))


#DEFENDERS 

sample = df_sample["Completed passes / 90"].to_numpy()

# sample mean, standard deviation, and sample size
x_bar = st.tmean(sample)
s = st.tstd(sample)
n = len(sample)

print("\nDEFENDERS (DF)")
print("Mean: %.2f. Standard deviation: %.2f. Size: %d." %
      (x_bar, s, n))

# standard error
std_err = s / math.sqrt(n)
print("Standard error: %.2f" % std_err)

# confidence level, significance level, and degrees of freedom
conf_lvl = 0.95
sig_lvl = 1 - conf_lvl
df = n - 1

print("Degrees of freedom: %d" % df)
print("Confidence level: %.2f" % conf_lvl)
print("Significance level: %.2f" % sig_lvl)

# confidence interval with t-distribution
ci_low_t, ci_upp_t = stm._tconfint_generic(
    x_bar,
    std_err,
    df,
    alpha=sig_lvl,
    alternative="two-sided"
)

print("C.I. (t*): %.2f to %.2f. Interval size: %.2f." %
      (ci_low_t, ci_upp_t, ci_upp_t-ci_low_t))