import pandas as pd
import matplotlib.pyplot as plt


# read saved random sample
data = pd.read_csv("T1_sample.csv")

# separate MF and DF samples
mf_sample = data[data["Position"] == "MF"]
df_sample = data[data["Position"] == "DF"]

# extract Completed Passes per 90 values
mf = mf_sample["Completed passes / 90"]
df = df_sample["Completed passes / 90"]


# MIDFIELDERS HISTOGRAM

mf_values = mf.values

mf_max = mf_values.max()
mf_min = mf_values.min()
mf_range = mf_max - mf_min

bin_width = 5
mf_bin_count = int(mf_range / bin_width)

plt.hist(mf_values, color='blue', edgecolor='black', bins=mf_bin_count)
plt.title("Histogram of Completed Passes per 90 - Midfielders")
plt.xlabel("Completed Passes per 90")
plt.ylabel("Players")
plt.show()


# DEFENDERS HISTOGRAM

df_values = df.values

df_max = df_values.max()
df_min = df_values.min()
df_range = df_max - df_min

bin_width = 5
df_bin_count = int(df_range / bin_width)

plt.hist(df_values, color='blue', edgecolor='black', bins=df_bin_count)
plt.title("Histogram of Completed Passes per 90 - Defenders")
plt.xlabel("Completed Passes per 90")
plt.ylabel("Players")
plt.show()