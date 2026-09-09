import pandas as pd

data = pd.read_csv("Players Stats.csv")

# Keep only players who played at least 90 minutes
data = data[data["Minutes Played"] >= 90]

# Separate MF and DF populations
mf_population = data[data["Position"] == "MF"]
df_population = data[data["Position"] == "DF"]

# Random sample of 115 from each group
mf_sample = mf_population.sample(n=115, random_state=42)
df_sample = df_population.sample(n=115, random_state=42)

# Select Completed Passes per 90
mf = mf_sample["Completed passes / 90"]
df = df_sample["Completed passes / 90"]


# MIDFIELDERS
mf_q1 = mf.quantile(0.25)
mf_q3 = mf.quantile(0.75)
mf_iqr = mf_q3 - mf_q1
mf_range = mf.max() - mf.min()

print("MIDFIELDERS (MF)")
print("Sample Size:", mf.count())
print("Mean:", round(mf.mean(), 2))
print("Median:", round(mf.median(), 2))
print("Mode:", round(mf.mode().iloc[0], 2))
print("Sample Variance:", round(mf.var(ddof=1), 2))
print("Standard Deviation:", round(mf.std(ddof=1), 2))
print("Minimum:", round(mf.min(), 2))
print("Maximum:", round(mf.max(), 2))
print("Range:", round(mf_range, 2))
print("Q1:", round(mf_q1, 2))
print("Q3:", round(mf_q3, 2))
print("IQR:", round(mf_iqr, 2))


# DEFENDERS
df_q1 = df.quantile(0.25)
df_q3 = df.quantile(0.75)
df_iqr = df_q3 - df_q1
df_range = df.max() - df.min()

print("\nDEFENDERS (DF)")
print("Sample Size:", df.count())
print("Mean:", round(df.mean(), 2))
print("Median:", round(df.median(), 2))
print("Mode:", round(df.mode().iloc[0], 2))
print("Sample Variance:", round(df.var(ddof=1), 2))
print("Standard Deviation:", round(df.std(ddof=1), 2))
print("Minimum:", round(df.min(), 2))
print("Maximum:", round(df.max(), 2))
print("Range:", round(df_range, 2))
print("Q1:", round(df_q1, 2))
print("Q3:", round(df_q3, 2))
print("IQR:", round(df_iqr, 2))

# MIDFIELDERS OUTLIER DETECTION
mf_lower = mf_q1 - (1.5 * mf_iqr)
mf_upper = mf_q3 + (1.5 * mf_iqr)

mf_outliers = mf[(mf < mf_lower) | (mf > mf_upper)]

print("\nMIDFIELDERS OUTLIERS")
print("Lower Bound:", round(mf_lower, 2))
print("Upper Bound:", round(mf_upper, 2))
print("Outliers:")
print(mf_outliers)


# DEFENDERS OUTLIER DETECTION
df_lower = df_q1 - (1.5 * df_iqr)
df_upper = df_q3 + (1.5 * df_iqr)

df_outliers = df[(df < df_lower) | (df > df_upper)]

print("\nDEFENDERS OUTLIERS")
print("Lower Bound:", round(df_lower, 2))
print("Upper Bound:", round(df_upper, 2))
print("Outliers:")
print(df_outliers)