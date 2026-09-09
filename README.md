FIFA World Cup 2026 - Completed Passes Analysis

Analytic Question

On average, is there a statistically significant difference in
completed passes per 90 minutes between midfielders and defenders at the
FIFA World Cup 2026?

Analysis Overview

Completed passes per 90 minutes was used to make the comparison fair
because players had different amounts of playing time. Comparing total
completed passes could favour players who played more minutes.

Formula:

Completed Passes per 90 = (Completed Passes / Minutes Played) × 90

Players who played less than 90 minutes were filtered out. Completed
passes per 90 was calculated to standardise passing performance across
different playing times.

Data Preparation and Sampling

Group                Eligible Population   Random Sample

Midfielders (MF)                     248             115
Defenders (DF)                       275             115
Total                        523         230

Simple random sampling was used to select 115 players from each group.
random_state=42 was used to make the random selection reproducible.

Python Files

File                                Purpose

descriptive_stats.py              Calculates descriptive statistics
for midfielders and defenders

histogram.py                      Creates histograms of completed
passes per 90

confidence_interval.py            Calculates the 95% confidence
intervals

Descriptive Statistics

Statistic              Midfielders (MF)   Defenders (DF)

Sample Size (n)                     115              115
Mean                              33.93            38.96
Median                            31.48            37.32
Mode                              24.17            30.00
Sample Variance                  243.77           241.45
Standard Deviation                15.61            15.54
Minimum                            3.85             5.82
Maximum                           85.96            80.95
Q1                                22.04            27.98
Q3                                44.28            48.51
IQR                               22.24            20.53

In the sample, defenders completed about 5.03 more passes per 90
minutes on average than midfielders.

Histograms

Midfielders (MF)



The midfielder histogram shows a positively (right) skewed
distribution. Most players are concentrated at lower-to-middle
completed passes per 90 values, while a few high values extend the tail
to the right. This is supported by the mean (33.93) being greater
than the median (31.48).

Defenders (DF)



The defender histogram shows a slightly positively (right) skewed
distribution. Most players are concentrated around the middle
completed passes per 90 values, while a few higher values extend the
tail to the right. This is supported by the mean (38.96) being
slightly greater than the median (37.32).

95% Confidence Interval

Group                 Mean   Lower Limit   Upper Limit   Interval Size

Midfielders (MF)     33.93         31.04         36.81            5.77
Defenders (DF)       38.96         36.09         41.83            5.74

At the 95% confidence level, the estimated population mean ranges from
31.04 to 36.81 completed passes per 90 for midfielders and 36.09
to 41.83 for defenders.

Two-Sample t-Test (Independent t-Test)

Step 1: State

The analytic question investigates whether midfielders and defenders
differ in their average completed passes per 90 minutes.

Step 2: Plan

A two-sided independent two-sample t-test was used because the question
investigates whether there is a difference without specifying which
group should have a higher mean.

Hypothesis                          Statement

H₀: μMF = μDF                   There is no difference in the
population mean completed passes
per 90 between midfielders and
defenders.

Step 3: Solve

Statistic                 MF      DF

Sample Size              115     115
Mean                   33.93   38.96
Standard Deviation     15.61   15.54

Test Result                        Value

t-statistic (t*)                  -2.45
p-value                           0.0151
Significance level (α)              0.05
Decision                   Reject H₀

Since 0.0151 < 0.05, the null hypothesis is rejected.

Step 4: Conclude

There is statistically significant evidence that midfielders and
defenders differ in their average completed passes per 90 minutes.
Defenders recorded a higher sample mean (38.96) than midfielders
(33.93).