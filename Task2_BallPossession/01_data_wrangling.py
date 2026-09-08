"""
FIFA World Cup 2026 - Possession vs Match Outcome
Task: Data Wrangling

Reads the raw collected match data (18 stacked mini-tables from Group A to
Final), extracts genuine match rows, auto-detects team-name misspellings
against a master reference list using fuzzy string matching, fixes a known
self-match data-entry error, standardizes result labels and dates, and
converts possession from a decimal fraction to a whole percentage.
"""

import pandas as pd
from difflib import get_close_matches

# Step 1: Load raw data and extract genuine match rows
# The raw file stacks 18 separate group/round tables in one sheet, each with
# its own repeated header row and blank separator rows. We keep only rows
# where Result is win/lose/draw, since that's what a real match row looks like.
raw = pd.read_excel('posession.xlsx', header=None)
raw.columns = ['Team', 'Opponent', 'Date', 'Result', 'Possession%', 'c5', 'c6', 'c7']

mask = raw['Result'].astype(str).str.lower().str.strip().isin(['win', 'lose', 'draw'])
df = raw.loc[mask, ['Team', 'Opponent', 'Date', 'Result', 'Possession%']].reset_index(drop=True)
print("Extracted match rows:", df.shape)

# Collapse any internal double-spaces (e.g. "South  Africa" -> "South Africa")
# before fuzzy matching, so whitespace typos don't get miscounted as separate teams.
df['Team'] = df['Team'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
df['Opponent'] = df['Opponent'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

# Step 2: Auto-detect misspelled team names against a master list
# The 48 real teams at FIFA World Cup 2026, correctly spelled.
master_teams = [
    'Algeria', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Bosnia and Herzegovina',
    'Brazil', 'Cabo Verde', 'Canada', 'Colombia', 'Congo DR', "Cote d'Ivoire", 'Croatia',
    'Curacao', 'Czechia', 'Ecuador', 'Egypt', 'England', 'France', 'Germany', 'Ghana',
    'Haiti', 'IR Iran', 'Iraq', 'Japan', 'Jordan', 'Korea Republic', 'Mexico', 'Morocco',
    'Netherlands', 'New Zealand', 'Norway', 'Panama', 'Paraguay', 'Portugal', 'Qatar',
    'Saudi Arabia', 'Scotland', 'Senegal', 'South Africa', 'Spain', 'Sweden', 'Switzerland',
    'Tunisia', 'Turkiye', 'USA', 'Uruguay', 'Uzbekistan',
]

def find_misspellings(names, master_list):
    # Compare every unique name against the master list, flag anything that
    # isn't an exact match, and suggest the closest correct spelling.
    unique_names = sorted(set(names))
    found = {}
    for name in unique_names:
        clean_name = ' '.join(str(name).split())
        if clean_name not in master_list:
            match = get_close_matches(clean_name, master_list, n=1, cutoff=0.6)
            found[name] = match[0] if match else 'NO MATCH FOUND'
    return found

all_names = list(df['Team']) + list(df['Opponent'])
misspellings = find_misspellings(all_names, master_teams)
print(f"\nAuto-detected {len(misspellings)} misspelled/inconsistent team names:")
for wrong, correct in misspellings.items():
    print(f"  '{wrong}' -> '{correct}'")

# Step 3: Apply the corrections
name_fixes = {wrong: correct for wrong, correct in misspellings.items()
              if correct != 'NO MATCH FOUND'}
df['Team'] = df['Team'].replace(name_fixes)
df['Opponent'] = df['Opponent'].replace(name_fixes)

# Step 4: Fix a known self-match data-entry error
# "Congo DR vs Congo DR" should really be "Congo DR vs Colombia".
df.loc[(df['Team'] == 'Congo DR') & (df['Opponent'] == 'Congo DR'), 'Opponent'] = 'Colombia'

# Step 5: Standardize Result column to lowercase
df['Result'] = df['Result'].astype(str).str.lower().str.strip()

# Step 6: Convert possession from decimal fraction to whole percentage
df['Possession%'] = (df['Possession%'].astype(float) * 100).round().astype(int)

# Step 7: Standardize dates to YYYY-MM-DD
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

# Step 8: Validation checks
print("\nValidation checks")
print("Missing values:\n", df.isnull().sum())
print("Result categories:", df['Result'].unique())
print("Self-matches remaining:", (df['Team'] == df['Opponent']).sum())
print("Unique teams:", pd.concat([df['Team'], df['Opponent']]).nunique())
print("Possession% range:", df['Possession%'].min(), "-", df['Possession%'].max())
print("Duplicate rows:", df.duplicated().sum())

# Save the cleaned dataset
df.to_csv('fifa_possession_clean.csv', index=False)
print("\nSaved fifa_possession_clean.csv - shape:", df.shape)
print(df['Result'].value_counts())