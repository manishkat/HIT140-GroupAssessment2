FIFA World Cup 2026: Attempts at Goal Analysis
S226_HIT140, Group 76

1. Analytic Question

The question I wanted to answer was whether there is a statistically significant difference, on average, in attempts at goal between UEFA (European) and CAF (African) players at the FIFA World Cup 2026.

I went with attempts at goal rather than goals scored, shots on target or shot accuracy because I was interested in attacking intent, basically how often a player actually tries to score, not how good they are at finishing. I also decided not to convert it into a per 90 minute rate the way you might with something like passes, since attempts at goal is the variable I'm studying directly and it isn't really being distorted by playing time in the same way a passing count would be. I do come back to this as a limitation later on, since players who were on the pitch longer naturally get more chances to shoot.

2. Data Wrangling

I pulled player statistics from fifa.com's official Player Statistics page for the 2026 World Cup, keeping only UEFA and CAF outfield players since that's who this comparison is about. From there I kept the columns that actually mattered for the analysis, being player name, country, confederation, position and attempts_at_goal, and dropped everything else. I double checked that attempts_at_goal was stored as a whole number, since it's a count and shouldn't have decimals, and went through the data looking for duplicate players or missing values. I didn't find any once the confederation filter had been applied. I also didn't cut anyone out for low minutes played, because attempts at goal is the thing I'm actually studying here, not a rate that needs a playing time cutoff to make sense.

3. Data Preparation and Sampling

This is where my approach differs a bit from a typical random sampling setup. Rather than drawing a random sample of players, I used every UEFA and CAF outfield player who appeared on fifa.com's stats page for the tournament, so what I'm looking at is a full census, not a subset.

| Group | Eligible Population | Used in Analysis |
|---|---|---|
| UEFA | 156 | 156 |
| CAF | 76 | 76 |
| Total | 232 | 232 |

Because I used the whole population instead of a random sample, the usual logic behind confidence intervals and t tests, which assumes you've randomly sampled from some bigger unseen population, doesn't quite apply here in the strict textbook sense. What I'm really testing is whether the pattern I see among these 232 players reflects a genuine difference in how the two confederations approach attacking play, rather than making a claim about a larger group of players these 232 were randomly drawn from. It's also worth mentioning that the dataset doesn't account for minutes played, so some of the gap I find later could come down to squad depth and rotation rather than individual players being more shot happy.

For a bit of context, here's how the two groups split by position.

| Confederation | Defender | Midfielder | Forward |
|---|---|---|---|
| UEFA | 37 | 58 | 61 |
| CAF | 14 | 31 | 31 |

4. Descriptive Statistics

| Statistic | UEFA | CAF |
|---|---|---|
| Sample Size (n) | 156 | 76 |
| Mean | 6.077 | 4.658 |
| Median | 4.0 | 4.0 |
| Sample Variance | 33.989 | 10.311 |
| Standard Deviation | 5.830 | 3.211 |
| Minimum | 1 | 1 |
| Maximum | 41 | 17 |

The gap between the two means was:

6.077 - 4.658 = 1.419

So UEFA players attempted about 1.42 more shots on goal on average than CAF players over the tournament. Interestingly, the medians don't show much of a gap at all, both sitting at exactly 4.0, which tells us the difference in means is probably being driven by a handful of high volume attackers on the UEFA side rather than a shift across the whole group. The standard deviations back this up too, UEFA's is 5.830 against CAF's 3.211, which is quite a bit higher, and that's the reason I used Welch's unequal variance versions of the confidence interval and t test in sections 6 and 7 instead of the standard pooled ones.

A quick note here, I didn't calculate mode, Q1, Q3 or IQR for this dataset since they weren't part of my original descriptive stats script, so I've left them out rather than guessing. They'd be easy enough to add with a couple of extra pandas lines if needed later.

Top 5 by confederation

| Rank | UEFA | Country | Attempts | CAF | Country | Attempts |
|---|---|---|---|---|---|---|
| 1 | Kylian Mbappe | France | 41 | Ismaila Sarr | Senegal | 17 |
| 2 | Lamine Yamal | Spain | 27 | Achraf Hakimi | Morocco | 14 |
| 3 | Mikel Oyarzabal | Spain | 23 | Ibrahim Maza | Algeria | 11 |
| 4 | Harry Kane | England | 23 | Yoane Wissa | DR Congo | 11 |
| 5 | Ousmane Dembele | France | 20 | Omar Marmoush | Egypt | 11 |

5. Histogram

Distribution of Attempts at Goal, UEFA vs CAF

Instead of building two separate histograms for each group, I plotted UEFA and CAF on the same axes so it's easier to compare them side by side, with each group's mean marked as a dashed line. What jumps out straight away is how right skewed UEFA's distribution is, most players sitting in the low to middle range but with a long tail stretching all the way out to Mbappe's 41 attempts. That lines up with UEFA's mean (6.077) sitting well above its median (4.0). CAF is also a bit right skewed, but far more tightly bunched together, with a much shorter tail that tops out at 17, and its mean (4.658) only just edges above its median (4.0).

6. Inferential Statistics: 95% Confidence Interval

Individual group means

| Group | Mean | Lower Limit | Upper Limit | Interval Width |
|---|---|---|---|---|
| UEFA | 6.077 | 5.155 | 6.999 | 1.844 |
| CAF | 4.658 | 3.924 | 5.392 | 1.467 |

At the 95 percent confidence level, I'd expect the true UEFA population mean to fall somewhere between 5.155 and 6.999 attempts at goal, and the CAF population mean between 3.924 and 5.392. UEFA's interval comes out a touch wider than CAF's, 1.844 against 1.467, which makes sense given UEFA has the bigger standard deviation of the two.

Difference in means

| | Value |
|---|---|
| Difference (UEFA - CAF) | 1.419 |
| Lower Limit | 0.247 |
| Upper Limit | 2.591 |

The interval that really matters for my question is the one built directly around the difference, mu_UEFA minus mu_CAF, using Welch's formula since the two groups' variances are quite different. That gave us a 95 percent CI of (0.247, 2.591). Since the whole range sits above zero, it looks like UEFA players attempt somewhere between about a quarter of a shot and just over two and a half more shots on average than CAF players, and a difference of zero really doesn't fit with what the data is showing.

7. Inferential Statistics: Two-Sample t-Test

Step 1: State

My analytic question was whether there's a statistically significant difference, on average, in attempts at goal between UEFA and CAF players at the FIFA World Cup 2026.

Step 2: Plan

Since I was asking whether any difference exists at all, not predicting which group would come out higher, I used a two sided independent two sample t test. Because the two groups' variances are quite different from each other, 33.989 for UEFA against 10.311 for CAF, I went with Welch's version of the t test rather than the standard pooled variance one, since Welch's doesn't require the two groups to have equal variances.

Hypotheses:

H0: mu_UEFA = mu_CAF
There's no difference in the population mean attempts at goal between UEFA and CAF players.

Ha: mu_UEFA is not equal to mu_CAF
There is a difference in the population mean attempts at goal between UEFA and CAF players.

Step 3: Solve

| Statistic | UEFA | CAF |
|---|---|---|
| Sample Size | 156 | 76 |
| Mean | 6.077 | 4.658 |
| Standard Deviation | 5.830 | 3.211 |

Running the test gave us:

| Test Result | Value |
|---|---|
| t-statistic (t*) | 2.387 |
| Degrees of Freedom (Welch-Satterthwaite) | 226.6 |
| p-value | 0.0178 |
| Significance Level (alpha) | 0.05 |
| Decision | Reject H0 |

Since 0.0178 is less than 0.05, I reject the null hypothesis.

Step 4: Conclude

Because the p value (0.0178) came in under 0.05, I reject H0. That means there's statistically significant evidence that UEFA and CAF players differ in how many attempts at goal they average.

UEFA players came out with the higher sample mean, 6.077 against CAF's 4.658, and this backs up what I found with the confidence interval in section 6, since an interval excluding zero at 95 percent confidence lines up with rejecting the null hypothesis at the 0.05 level in a two tailed test. They're basically two different ways of arriving at the same answer.

Limitations

A few things are worth keeping in mind before taking these results too far. This is a census of the players fifa.com published, not a random sample, so the usual sampling assumptions behind confidence intervals and t tests don't strictly hold, and my conclusions are really about this particular group of 232 players rather than some wider population. The dataset also includes every listed player no matter how many minutes they played, so part of the gap I found could be down to squad rotation depth rather than every individual being more shot happy, and I didn't normalise attempts at goal to a per 90 minute rate the way you'd want to for something like completed passes. And finally, all this tells us is how many shots players attempted, not how accurate or clinical they were in front of goal.
