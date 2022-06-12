import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('QueryResults.csv')

df = df.rename(columns={"m": "DATE", 'TagName': "TAG", 'Unnamed: 2': "POSTS"})

# df.DATE = pd.to_datetime(df.DATE[1])

# df.head()
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
# df.groupby('TAG').sum().sort_values(by='POSTS',ascending=False)

reshaped_df.fillna(0, inplace=True)

# reshaped_df.isna().values.any()

# SHARP
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)
plt.legend(fontsize=16)

# SMOOTH

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=16)
