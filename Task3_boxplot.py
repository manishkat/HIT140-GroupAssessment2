# Task3_boxplot.py
# S226_HIT140 - Group 76
# Boxplot of attempts_at_goal for UEFA vs CAF players at the
# FIFA World Cup 2026, showing median, IQR, whiskers and outliers
# for each confederation side by side.

# Input : Task3_Players_Stats_sampled.csv (random sample of 38 UEFA and
#         38 CAF players drawn from Task3_Players_Stats.csv, see Task3_sample.py)
# Output: Task3_boxplot_attempts_at_goal.png


import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "Task3_Players_Stats_sampled.csv"
OUTPUT_FILE = "Task3_boxplot_attempts_at_goal.png"
VARIABLE = "attempts_at_goal"


def main():
    df = pd.read_csv(INPUT_FILE)
    df = df[df["confederation"].isin(["UEFA", "CAF"])]

    uefa = df[df["confederation"] == "UEFA"][VARIABLE]
    caf = df[df["confederation"] == "CAF"][VARIABLE]

    # print the actual quartiles being plotted, so they end up in the console
    # output and can be quoted directly in the report
    for label, series in [("UEFA", uefa), ("CAF", caf)]:
        q1, med, q3 = series.quantile([0.25, 0.5, 0.75])
        iqr = q3 - q1
        print(f"{label}: n={len(series)}  Q1={q1:.2f}  Median={med:.2f}  "
              f"Q3={q3:.2f}  IQR={iqr:.2f}  "
              f"whisker_low={max(series.min(), q1 - 1.5*iqr):.2f}  "
              f"whisker_high={min(series.max(), q3 + 1.5*iqr):.2f}")

    fig, ax = plt.subplots(figsize=(7, 5.5))
    box = ax.boxplot(
        [uefa, caf],
        tick_labels=[f"UEFA (n={len(uefa)})", f"CAF (n={len(caf)})"],
        patch_artist=True,
        widths=0.5,
        medianprops=dict(color="black", linewidth=1.5),
    )
    colors = ["#a3a364", "#0e68cf"]
    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel("Attempts at goal")
    ax.set_title("Attempts at Goal by Confederation: UEFA vs CAF\n"
                  "FIFA World Cup 2026")
    fig.tight_layout()
    fig.savefig(OUTPUT_FILE, dpi=150)
    print(f"\nBoxplot saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
