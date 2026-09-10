
# Task3_histogram.py
# S226_HIT140 - Group 76
# Histogram of attempts_at_goal for UEFA vs CAF players at the
# FIFA World Cup 2026, illustrating UEFA's longer right tail
# (driven by high-volume attackers such as Cristiano Ronaldo).

# Input : Task3_Players_Stats_sampled.csv (random sample of 38 UEFA and
#         38 CAF players drawn from Task3_Players_Stats.csv, see Task3_sample.py)
# Output: Task3_histogram_attempts_at_goal.png


import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "Task3_Players_Stats_sampled.csv"
OUTPUT_FILE = "Task3_histogram_attempts_at_goal.png"
VARIABLE = "attempts_at_goal"


def main():
    df = pd.read_csv(INPUT_FILE)
    df = df[df["confederation"].isin(["UEFA", "CAF"])]

    uefa = df[df["confederation"] == "UEFA"][VARIABLE]
    caf = df[df["confederation"] == "CAF"][VARIABLE]

    max_val = int(df[VARIABLE].max())
    bins = range(0, max_val + 2)  # integer bins, since attempts_at_goal is a count

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.hist(uefa, bins=bins, alpha=0.6, label=f"UEFA (n={len(uefa)})",
            color="#a3a364", edgecolor="white", align="left")
    ax.hist(caf, bins=bins, alpha=0.6, label=f"CAF (n={len(caf)})",
            color="#0e68cf", edgecolor="white", align="left")

    ax.axvline(uefa.mean(), color="#a3a364", linestyle="--", linewidth=1.5,
               label=f"UEFA mean = {uefa.mean():.2f}")
    ax.axvline(caf.mean(), color="#0e68cf", linestyle="--", linewidth=1.5,
               label=f"CAF mean = {caf.mean():.2f}")

    ax.set_xlabel("Attempts at goal")
    ax.set_ylabel("Number of players")
    ax.set_title("Distribution of Attempts at Goal: UEFA vs CAF\n"
                  "FIFA World Cup 2026")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_FILE, dpi=150)
    print(f"Histogram saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
