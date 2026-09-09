"""
Task 3 - Goalkeeping & Defensive Performance
Step 4: Histograms and Boxplot

Visualises the distribution of save % for each group (advanced vs eliminated)
on the n=33 stratified sample.
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("Result_screenshots", exist_ok=True)

df = pd.read_csv("fifa_SAMPLE_savepct_n33.csv")

adv = df.loc[df["advanced"] == True, "save_pct"]
elim = df.loc[df["advanced"] == False, "save_pct"]

# --- Histograms (one figure per group, matching the group's report style) ---
fig, ax = plt.subplots(figsize=(7, 5))
ax.hist(adv, bins=8, color="#2f6f4f", edgecolor="black", alpha=0.85)
ax.set_title("Histogram of Save % - Advanced to Knockout Stage (n=22)")
ax.set_xlabel("Save %")
ax.set_ylabel("Number of teams")
fig.tight_layout()
fig.savefig("Result_screenshots/histogram_advanced.png", dpi=150)
plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 5))
ax.hist(elim, bins=8, color="#a83232", edgecolor="black", alpha=0.85)
ax.set_title("Histogram of Save % - Eliminated in Group Stage (n=11)")
ax.set_xlabel("Save %")
ax.set_ylabel("Number of teams")
fig.tight_layout()
fig.savefig("Result_screenshots/histogram_eliminated.png", dpi=150)
plt.close(fig)

# --- Side-by-side boxplot ---
fig, ax = plt.subplots(figsize=(7, 5))
ax.boxplot([adv, elim], tick_labels=["Advanced (n=22)", "Eliminated (n=11)"],
           patch_artist=True,
           boxprops=dict(facecolor="#dce6f1"))
ax.set_title("Save % by Tournament Outcome")
ax.set_ylabel("Save %")
fig.tight_layout()
fig.savefig("Result_screenshots/boxplot_savepct.png", dpi=150)
plt.close(fig)

print("Saved:")
print(" - Result_screenshots/histogram_advanced.png")
print(" - Result_screenshots/histogram_eliminated.png")
print(" - Result_screenshots/boxplot_savepct.png")

print(f"\nAdvanced group skew check: mean={adv.mean():.2f}, median={adv.median():.2f}")
print(f"Eliminated group skew check: mean={elim.mean():.2f}, median={elim.median():.2f}")
