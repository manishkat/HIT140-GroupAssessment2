import pandas as pd
import matplotlib.pyplot as plt

# read saved random sample
data = pd.read_csv("T1_sample.csv")

# separate MF and DF samples
mf_sample = data[data["Position"] == "MF"]["Completed passes / 90"]
df_sample = data[data["Position"] == "DF"]["Completed passes / 90"]

# create boxplot
plt.figure(figsize=(8, 6))

plt.boxplot(
    [mf_sample, df_sample],
    tick_labels=["Midfielders (MF)", "Defenders (DF)"]
)

plt.title("Completed Passes per 90: Midfielders vs Defenders")
plt.ylabel("Completed Passes per 90")
plt.xlabel("Position")

plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.show()