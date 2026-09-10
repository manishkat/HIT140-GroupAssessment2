"""
Task 3 - Goalkeeping & Defensive Performance
Step 1: Data Wrangling

Analytic question:
On average, is there a statistically significant difference in save percentage
between goalkeepers whose team advanced to the knockout stage and goalkeepers
whose team was eliminated in the group stage at the FIFA World Cup 2026?

Inputs (raw, as scraped from FIFA.com's official team goalkeeping stats and
cross-checked against Al Jazeera / Wikipedia's Round of 32 qualifier list -
see sources.md):
    raw_team_goalkeeping_stats.csv   - 48 teams, clean sheets, goals conceded,
                                        goalkeeper saves, goalkeeping actions
                                        inside/outside the penalty area
    round_of_32_qualifiers.csv       - the 32 teams that reached the knockout
                                        rounds (Round of 32 or beyond)

Output:
    fifa_team_savepct_advanced_vs_eliminated.csv - wrangled 48-team population,
        with save_pct engineered and each team labelled advanced / eliminated

Save % is not published directly by these sources, so it is engineered as:
    save_pct = goalkeeper_saves / (goalkeeper_saves + goals_conceded) * 100
which is the standard approximation for saves / shots-on-target-against used
by mainstream football statistics providers, since shots on target against =
saves + goals conceded.
"""

import os
import pandas as pd

# Always resolve paths relative to this script's own folder, regardless of
# what directory the interpreter was launched from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

raw = pd.read_csv("raw_team_goalkeeping_stats.csv")
qualifiers = pd.read_csv("round_of_32_qualifiers.csv")

print("Raw team goalkeeping stats:", raw.shape)
print(raw.head(), "\n")

print("Round of 32 qualifiers (advanced teams):", qualifiers.shape)
print(qualifiers.head(), "\n")

# Feature engineering: derive save percentage
raw["save_pct"] = raw["goalkeeper_saves"] / (raw["goalkeeper_saves"] + raw["goals_conceded"]) * 100

# Label each team advanced / eliminated by checking Round of 32 membership
advanced_teams = set(qualifiers["team"])
raw["advanced"] = raw["team"].isin(advanced_teams)

# Sanity checks
n_missing = raw["save_pct"].isna().sum()
print(f"Rows with missing save_pct after wrangling: {n_missing}")
print(f"Teams advanced: {raw['advanced'].sum()}  |  Teams eliminated: {(~raw['advanced']).sum()}")

# Reorder columns to match the reporting convention used across the group project
wrangled = raw[["rank", "team", "clean_sheets", "goals_conceded", "goalkeeper_saves",
                 "gk_actions_inside_pa", "gk_actions_outside_pa", "save_pct", "advanced"]]

wrangled.to_csv("fifa_team_savepct_advanced_vs_eliminated.csv", index=False)

print("\nWrangled population dataset (first 5 rows):")
print(wrangled.head())
print(f"\nSaved -> fifa_team_savepct_advanced_vs_eliminated.csv  ({wrangled.shape[0]} teams, full 2026 population)")
