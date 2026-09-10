# Task3_sample.py
# S226_HIT140 - Group 76
# Draws a random sample of 38 UEFA players and 38 CAF players from the
# full Task3_Players_Stats.csv population, using a fixed random seed so
# the sample is reproducible. This sampled file feeds all the other
# T3 scripts (descriptive stats, boxplot, histogram, confidence
# interval, two sample t test) for the sampling-based version of the
# analysis.

# Input : Task3_Players_Stats.csv
# Output: Task3_Players_Stats_sampled.csv

import pandas as pd

INPUT_FILE = "Task3_Players_Stats.csv"
OUTPUT_FILE = "Task3_Players_Stats_sampled.csv"
SEED = 42
N_PER_GROUP = 38

df = pd.read_csv(INPUT_FILE)
df = df[df["confederation"].isin(["UEFA", "CAF"])]

uefa_sample = df[df["confederation"] == "UEFA"].sample(n=N_PER_GROUP, random_state=SEED)
caf_sample = df[df["confederation"] == "CAF"].sample(n=N_PER_GROUP, random_state=SEED)

sampled = pd.concat([uefa_sample, caf_sample]).sort_values(["confederation", "rank"])
sampled.to_csv(OUTPUT_FILE, index=False)
print(f"UEFA sample: {len(uefa_sample)}, CAF sample: {len(caf_sample)}")
print(f"Saved to {OUTPUT_FILE}")

# position breakdown for the sample
print(pd.crosstab(sampled["confederation"], sampled["position"]))
