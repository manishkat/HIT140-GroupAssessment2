import scipy.stats as st

# basic statistics of sample 1: Midfielders
x_bar1 = 33.93
s1 = 15.61
n1 = 115

# basic statistics of sample 2: Defenders
x_bar2 = 38.96
s2 = 15.54
n2 = 115

# perform two-sample t-test
# null hypothesis: mean completed passes per 90 of MF = mean of DF
# alternative hypothesis: mean completed passes per 90 of MF != mean of DF
# equal_var=False assumes that the two populations do not have equal variance
t_stats, p_val = st.ttest_ind_from_stats(
    x_bar1, s1, n1,
    x_bar2, s2, n2,
    equal_var=False,
    alternative='two-sided'
)

print("\n Computing t* ...")
print("\t t-statistic (t*): %.2f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.4f" % p_val)

print("\n Conclusion:")
if p_val < 0.05:
    print("\t We reject the null hypothesis.")
else:
    print("\t We accept the null hypothesis.")