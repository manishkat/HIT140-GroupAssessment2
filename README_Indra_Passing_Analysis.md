# FIFA World Cup 2026 – Completed Passes Analysis

## 1. Analytic Question

**On average, is there a statistically significant difference in completed passes per 90 minutes between midfielders and defenders at the FIFA World Cup 2026?**

Completed passes per 90 minutes was used to make the comparison fair because players had different amounts of playing time. Comparing total completed passes could favour players who played more minutes.

**Formula:**

`Completed Passes per 90 = (Completed Passes / Minutes Played) × 90`

---

## 2. Data Wrangling

Player statistics were collected for midfielders and defenders who participated in the FIFA World Cup 2026. Relevant variables such as position, minutes played and completed passes were retained.

Players who played less than 90 minutes were filtered out. Completed passes per 90 minutes was then calculated to standardise passing performance across different playing times.

---

## 3. Data Preparation and Sampling

The eligible players were divided into midfielder (MF) and defender (DF) populations. Simple random sampling was used to select 115 players from each group. `random_state=42` was used to make the random selection reproducible.

| Group | Eligible Population | Random Sample |
|---|---:|---:|
| Midfielders (MF) | 248 | 115 |
| Defenders (DF) | 275 | 115 |
| **Total** | **523** | **230** |

---

## 4. Descriptive Statistics

| Statistic | Midfielders (MF) | Defenders (DF) |
|---|---:|---:|
| Sample Size (n) | 115 | 115 |
| Mean | 33.93 | 38.96 |
| Median | 31.48 | 37.32 |
| Mode | 24.17 | 30.00 |
| Sample Variance | 243.77 | 241.45 |
| Standard Deviation | 15.61 | 15.54 |
| Minimum | 3.85 | 5.82 |
| Maximum | 85.96 | 80.95 |
| Q1 | 22.04 | 27.98 |
| Q3 | 44.28 | 48.51 |
| IQR | 22.24 | 20.53 |

The main difference between the sample means was:

`38.96 - 33.93 = 5.03`

Therefore, defenders completed about **5.03 more passes per 90 minutes on average** than midfielders in the sample.

The median shows a similar pattern, with **37.32 for defenders** compared with **31.48 for midfielders**. The standard deviations are almost identical (**15.54 vs 15.61**), indicating similar variation between the two groups.

---

## 5. Histograms

### Midfielders (MF)

![Histogram of Completed Passes per 90 - Midfielders](histogram_midfielders.png)

The histogram shows a **positively skewed (right-skewed) distribution**. Most players are concentrated at lower-to-middle completed passes per 90 values, while a few high values extend the tail to the right. This is also supported by the mean (**33.93**) being greater than the median (**31.48**).

### Defenders (DF)

![Histogram of Completed Passes per 90 - Defenders](histogram_defenders.png)

The histogram shows a **slightly positively skewed (right-skewed) distribution**. Most players are concentrated around the middle completed passes per 90 values, while a few higher values extend the tail to the right. This is supported by the mean (**38.96**) being slightly greater than the median (**37.32**).

---

## 6. Inferential Statistics – 95% Confidence Interval

| Group | Mean | Lower Limit | Upper Limit | Interval Size |
|---|---:|---:|---:|---:|
| Midfielders (MF) | 33.93 | 31.04 | 36.81 | 5.77 |
| Defenders (DF) | 38.96 | 36.09 | 41.83 | 5.74 |

At the **95% confidence level**, the estimated population mean for midfielders ranges from **31.04 to 36.81 completed passes per 90**. For defenders, it ranges from **36.09 to 41.83**.

The confidence interval widths are **5.77 for MF** and **5.74 for DF**, indicating very similar precision between the two estimates.

---

## 7. Inferential Statistics – Two-Sample t-Test

### Step 1: State

**Analytic Question:**

On average, is there a statistically significant difference in completed passes per 90 minutes between midfielders and defenders at the FIFA World Cup 2026?

### Step 2: Plan

Since the question investigates whether there is a difference without specifying which group should have a higher mean, a **two-sided independent two-sample t-test** was used.

**Hypotheses:**

**H₀: μMF = μDF**

There is no difference in the population mean completed passes per 90 between midfielders and defenders.

**Hₐ: μMF ≠ μDF**

There is a difference in the population mean completed passes per 90 between midfielders and defenders.

### Step 3: Solve

| Statistic | MF | DF |
|---|---:|---:|
| Sample Size | 115 | 115 |
| Mean | 33.93 | 38.96 |
| Standard Deviation | 15.61 | 15.54 |

The test produced:

| Test Result | Value |
|---|---:|
| t-statistic (t*) | -2.45 |
| p-value | 0.0151 |
| Significance Level (α) | 0.05 |
| Decision | **Reject H₀** |

Since **0.0151 < 0.05**, the null hypothesis is rejected.

### Step 4: Conclude

Since the **p-value (0.0151) is less than 0.05**, the null hypothesis is rejected. Therefore, there is **statistically significant evidence that midfielders and defenders differ in their average completed passes per 90 minutes**.

Defenders recorded a higher sample mean (**38.96**) than midfielders (**33.93**).
