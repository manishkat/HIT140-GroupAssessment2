
# Task3_descriptive_stats.py
# S226_HIT140 - Group 76
# Descriptive statistics for the FIFA World Cup 2026 "Attempts at Goal"
# analytic task (UEFA vs CAF).

# Input : Task3_Players_Stats_sampled.csv (random sample of 38 UEFA and
#         38 CAF players drawn from Task3_Players_Stats.csv, see Task3_sample.py)
#         columns -> rank, player, country, confederation, position, attempts_at_goal
# Output: prints the group summary table and the top-5-per-confederation
   #     table to the console, and writes Task3_descriptive_stats_summary.csv


import pandas as pd

INPUT_FILE = "Task3_Players_Stats_sampled.csv"
OUTPUT_FILE = "Task3_descriptive_stats_summary.csv"
VARIABLE = "attempts_at_goal"
GROUPS = ["UEFA", "CAF"]


def main():
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")
    print("Confederations present:", df["confederation"].unique())

    df = df[df["confederation"].isin(GROUPS)]

    # --- Group summary (mean, median, SD, min, max) ---
    summary = df.groupby("confederation")[VARIABLE].agg(
        ["count", "mean", "median", "std", "min", "max"]
    ).round(3)

    # --- Quartiles, IQR, and variance ---
    q1 = df.groupby("confederation")[VARIABLE].quantile(0.25)
    q3 = df.groupby("confederation")[VARIABLE].quantile(0.75)
    var = df.groupby("confederation")[VARIABLE].var(ddof=1)

    summary["q1"] = q1
    summary["q3"] = q3
    summary["iqr"] = q3 - q1
    summary["variance"] = var
    summary = summary.round(3)

    summary = summary.reindex(GROUPS)

    print("\n" + "=" * 60)
    print(f"Descriptive Statistics: {VARIABLE} by confederation")
    print("=" * 60)
    print(summary.to_string())

    for confed in GROUPS:
        m = summary.loc[confed, "mean"]
        med = summary.loc[confed, "median"]
        skew_note = "right-skewed" if m > med else "roughly symmetric/left-skewed"
        print(f"{confed}: mean ({m}) vs median ({med}) -> {skew_note}")

    summary.to_csv(OUTPUT_FILE)
    print(f"\nSummary written to {OUTPUT_FILE}")

    # --- Position breakdown (context table) ---
    pos_table = pd.crosstab(df["confederation"], df["position"])
    pos_table = pos_table.reindex(GROUPS)
    print("\n" + "=" * 60)
    print("Position breakdown by confederation")
    print("=" * 60)
    print(pos_table.to_string())

    # --- Top 5 players by attempts at goal, per confederation ---
    print("\n" + "=" * 60)
    print(f"Top 5 players by {VARIABLE}, per confederation")
    print("=" * 60)
    for confed in GROUPS:
        top5 = (
            df[df["confederation"] == confed]
            .sort_values(VARIABLE, ascending=False)
            .head(5)[["player", "country", "position", VARIABLE]]
        )
        print(f"\n-- {confed} --")
        print(top5.to_string(index=False))


if __name__ == "__main__":
    main()
