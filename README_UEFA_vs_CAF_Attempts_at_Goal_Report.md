FIFA World Cup 2026: Attempts at Goal Analysis
S226_HIT140, Group 76

1. Analytic Question

The question I wanted to answer was whether there is a statistically significant difference, on average, in attempts at goal between UEFA (European) and CAF (African) players at the FIFA World Cup 2026.

I went with attempts at goal rather than goals scored, shots on target or shot accuracy because I was interested in attacking intent, basically how often a player actually tries to score, not how good they are at finishing. I also decided not to convert it into a per 90 minute rate the way you might with something like passes, since attempts at goal is the variable I'm studying directly and it isn't really being distorted by playing time in the same way a passing count would be. I do come back to this as a limitation later on, since players who were on the pitch longer naturally get more chances to shoot.

2. Data Wrangling

I pulled player statistics from fifa.com's official Player Statistics page for the 2026 World Cup, keeping only UEFA and CAF outfield players since that's who this comparison is about. From there I kept the columns that actually mattered for the analysis, being player name, country, confederation, position and attempts_at_goal, and dropped everything else. I double checked that attempts_at_goal was stored as a whole number, since it's a count and shouldn't have decimals, and went through the data looking for duplicate players or missing values. I didn't find any once the confederation filter had been applied. I also didn't cut anyone out for low minutes played, because attempts at goal is the thing I'm actually studying here, not a rate that needs a playing time cutoff to make sense.

3. Data Preparation and Sampling

After filtering to UEFA and CAF outfield players, I had 156 UEFA players and 76 CAF players available. Rather than using every one of them as a census, I drew a random sample of 38 players from each confederation using pandas' sample method with a fixed random seed (42) so the sample can be reproduced exactly if the script is run again. I picked 38 because it's the largest number I could take from CAF, the smaller group, while still keeping the two samples the same size, which keeps the two sample t test and the confidence interval calculations balanced and easier to compare.

| Group | Eligible Population | Used in Analysis |
|---|---|---|
| UEFA | 156 | 38 |
| CAF | 76 | 38 |
| Total | 232 | 76 |

Because this is now a genuine random sample drawn from each confederation's player pool rather than the full population, the usual logic behind confidence intervals and t tests applies more comfortably than it did with the census approach, since both methods assume the data came from random sampling. What I'm testing here is whether the difference I see between these two samples of 38 players reflects a genuine difference between UEFA and CAF players generally, rather than just describing the specific 232 players who happened to be on fifa.com's list. The tradeoff is that a sample of 38 per group is a lot smaller than the full 156 and 76 I had access to, so there's more room for the two samples to look different (or similar) just by chance. The dataset also still doesn't account for minutes played, so some of any gap found could come down to squad depth and rotation rather than individual players being more shot happy.

For a bit of context, here's how the two sampled groups split by position.

| Confederation | Defender | Midfielder | Forward |
|---|---|---|---|
| UEFA | 8 | 16 | 14 |
| CAF | 4 | 17 | 17 |

4. Descriptive Statistics

| Statistic | UEFA | CAF |
|---|---|---|
| Sample Size (n) | 38 | 38 |
| Mean | 5.316 | 4.684 |
| Median | 3.5 | 4.0 |
| Sample Variance | 16.979 | 11.033 |
| Standard Deviation | 4.121 | 3.322 |
| Minimum | 1 | 1 |
| Maximum | 18 | 17 |

The gap between the two sample means was:

5.316 - 4.684 = 0.632

So in this sample, UEFA players attempted about 0.63 more shots on goal on average than CAF players, which is a much smaller gap than the 1.42 difference I found when I used the full population earlier. The medians tell a similar story to before, with CAF actually sitting slightly higher (4.0) than UEFA (3.5), which again points to a handful of high volume attackers pulling the UEFA mean up rather than a shift across the whole sample. UEFA's standard deviation (4.121) is still noticeably higher than CAF's (3.322), so I kept using Welch's unequal variance versions of the confidence interval and t test in sections 6 and 7.

Top 5 by confederation (within the sampled 38 per group)

| Rank | UEFA | Country | Attempts | CAF | Country | Attempts |
|---|---|---|---|---|---|---|
| 1 | Cristiano Ronaldo | Portugal | 18 | Ismaila Sarr | Senegal | 17 |
| 2 | Ferran Torres | Spain | 14 | Omar Marmoush | Egypt | 11 |
| 3 | Bukayo Saka | England | 13 | Ismael Saibari | Morocco | 10 |
| 4 | Viktor Gyokeres | Sweden | 12 | Mohamed Salah | Egypt | 9 |
| 5 | Marcus Rashford | England | 12 | Amad Diallo | Ivory Coast | 8 |

Mbappe, Yamal and Oyarzabal, who topped the UEFA list in the full population, didn't end up in this particular random draw, which is part of why the UEFA mean came down so much compared to the census version.

5. Histogram

Distribution of Attempts at Goal, UEFA vs CAF

I kept UEFA and CAF plotted on the same axes with each group's mean marked as a dashed line, same as before. The two distributions now sit a lot closer together than they did with the full population. UEFA still has a longer tail, topping out at Cristiano Ronaldo's 18 attempts, while CAF's tail is a touch shorter at 17 with Ismaila Sarr. The dashed mean lines for the two groups (5.32 for UEFA and 4.68 for CAF) are noticeably closer together than in the census version, which visually matches the smaller gap in section 4.

6. Inferential Statistics: 95% Confidence Interval

Individual group means

| Group | Mean | Lower Limit | Upper Limit | Interval Width |
|---|---|---|---|---|
| UEFA | 5.316 | 3.961 | 6.670 | 2.709 |
| CAF | 4.684 | 3.592 | 5.776 | 2.184 |

At the 95 percent confidence level, I'd expect the true UEFA population mean to fall somewhere between 3.961 and 6.670 attempts at goal, and the CAF population mean between 3.592 and 5.776. Both intervals are wider than the ones I got from the full population, which makes sense given each sample is now only 38 players instead of 156 or 76.

Difference in means

| | Value |
|---|---|
| Difference (UEFA - CAF) | 0.632 |
| Lower Limit | -1.080 |
| Upper Limit | 2.344 |

The interval that really matters for my question is the one built directly around the difference, mu_UEFA minus mu_CAF, using Welch's formula since the two groups' variances are still quite different. That gave us a 95 percent CI of (-1.080, 2.344). Because this interval crosses zero, a true difference of zero between the two confederations is entirely plausible given this sample, so I can't say with confidence that UEFA players attempt more shots on goal than CAF players based on this data alone.

7. Inferential Statistics: Two-Sample t-Test

Step 1: State

My analytic question was whether there's a statistically significant difference, on average, in attempts at goal between UEFA and CAF players at the FIFA World Cup 2026.

Step 2: Plan

Since I was asking whether any difference exists at all, not predicting which group would come out higher, I used a two sided independent two sample t test. Because the two groups' variances are still quite different from each other, 16.979 for UEFA against 11.033 for CAF, I went with Welch's version of the t test rather than the standard pooled variance one, since Welch's doesn't require the two groups to have equal variances.

Hypotheses:

H0: mu_UEFA = mu_CAF
There's no difference in the population mean attempts at goal between UEFA and CAF players.

Ha: mu_UEFA is not equal to mu_CAF
There is a difference in the population mean attempts at goal between UEFA and CAF players.

Step 3: Solve

| Statistic | UEFA | CAF |
|---|---|---|
| Sample Size | 38 | 38 |
| Mean | 5.316 | 4.684 |
| Standard Deviation | 4.121 | 3.322 |

Running the test gave us:

| Test Result | Value |
|---|---|
| t-statistic (t*) | 0.736 |
| Degrees of Freedom (Welch-Satterthwaite) | 70.8 |
| p-value | 0.4644 |
| Significance Level (alpha) | 0.05 |
| Decision | Fail to reject H0 |

Since 0.4644 is greater than 0.05, I fail to reject the null hypothesis.

Step 4: Conclude

Because the p value (0.4644) came in well above 0.05, I fail to reject H0. That means there isn't statistically significant evidence, based on this sample of 38 players per confederation, that UEFA and CAF players differ in how many attempts at goal they average.

UEFA still came out with the higher sample mean, 5.316 against CAF's 4.684, but the gap is small enough relative to the variability in each sample that it could plausibly be down to chance. This lines up with the confidence interval in section 6, since an interval that includes zero at 95 percent confidence goes hand in hand with failing to reject the null at the 0.05 level in a two tailed test.

It's worth noting how different this conclusion is from the one I got using the full population of 156 UEFA and 76 CAF players, where the difference came out significant. That earlier result was being driven by a small number of very high volume UEFA attackers like Mbappe and Yamal, and this random sample of 38 per group simply didn't happen to include most of them. This is a good illustration of how sample size and which players happen to get drawn can change the outcome of a test even when the underlying data hasn't changed.

Limitations

A few things are worth keeping in mind before taking these results too far. Cutting the sample down to 38 players per confederation means the test has less power to detect a real difference even if one exists, so failing to reject H0 here doesn't necessarily mean there's no difference at all between UEFA and CAF players, only that this particular sample didn't provide strong enough evidence of one. A different random seed would likely have pulled in a different mix of players and could easily have produced a different conclusion, which is something to be upfront about. The dataset also includes players regardless of minutes played, so part of any gap is still tangled up with squad rotation depth rather than every individual being more shot happy, and I didn't normalise attempts at goal to a per 90 minute rate the way you'd want to for something like completed passes. And finally, all this tells us is how many shots players attempted, not how accurate or clinical they were in front of goal.
