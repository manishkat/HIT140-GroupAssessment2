"""
FIFA World Cup 2026 - Possession vs Match Outcome
Task: Data Preparation and Sampling

Loads the cleaned match data, defines the population and the two groups
being compared, and draws a random sample of 40 matches from each group.
"""

import pandas as pd

# Load the cleaned dataset produced by 01_data_wrangling.py
df = pd.read_csv('fifa_possession_clean.csv')

# Population: all FIFA World Cup 2026 matches with recorded possession data.
# We only need win/lose rows for this comparison, so draws are excluded.
winners = df[df['Result'] == 'win']['Possession%']
losers = df[df['Result'] == 'lose']['Possession%']

print("Total winning-team rows available:", len(winners))
print("Total losing-team rows available:", len(losers))

# Draw a simple random sample of 40 from each group.
# random_state is fixed so the sample is reproducible.
sample_winners = winners.sample(n=40, random_state=42)
sample_losers = losers.sample(n=40, random_state=42)

print("\nSample of winners (n=40):")
print(sample_winners.describe())

print("\nSample of losers (n=40):")
print(sample_losers.describe())

# Save the samples so later scripts can reuse them without re-sampling
sample_winners.to_csv('sample_winners.csv', index=False)
sample_losers.to_csv('sample_losers.csv', index=False)
print("\nSaved sample_winners.csv and sample_losers.csv")