"""
Task 3 - Goalkeeping & Defensive Performance
Step 2: Data Preparation and Sampling

The 48 teams in fifa_team_savepct_advanced_vs_eliminated.csv are the full
FIFA World Cup 2026 population (all 48 competing nations), not a sample -
so a stratified random sample is drawn from it for the descriptive and
inferential analysis, preserving the population's 2:1 advanced:eliminated
ratio (32 advanced : 16 eliminated).

random_state=42 is fixed for reproducibility.
"""

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pop = pd.read_csv("fifa_team_savepct_advanced_vs_eliminated.csv")

advanced_pool = pop[pop["advanced"] == True]
eliminated_pool = pop[pop["advanced"] == False]

print(f"Population: {len(pop)} teams  "
      f"({len(advanced_pool)} advanced, {len(eliminated_pool)} eliminated)")

# Preserve the population's 2:1 ratio at a sample size of 33
# (68.75% of each stratum -> 22 advanced, 11 eliminated)
sample_advanced = advanced_pool.sample(n=22, random_state=42)
sample_eliminated = eliminated_pool.sample(n=11, random_state=42)

sample = pd.concat([sample_advanced, sample_eliminated]).sort_values("team").reset_index(drop=True)

print(f"\nStratified random sample drawn: n = {len(sample)} "
      f"({len(sample_advanced)} advanced, {len(sample_eliminated)} eliminated) "
      "-- preserves the 2:1 population ratio")

sample.to_csv("fifa_SAMPLE_savepct_n33.csv", index=False)
print("\nSample dataset (first 5 rows):")
print(sample.head())
print("\nSaved -> fifa_SAMPLE_savepct_n33.csv  (this is the dataset used for all analysis below)")
