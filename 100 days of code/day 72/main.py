#%%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('100 days of code//day 72//QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
df.DATE = pd.to_datetime(df.DATE)
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df.fillna(0, inplace=True)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.figure(figsize=(16,10)) 
plt.yticks(fontsize=14)
plt.plot(reshaped_df.index, reshaped_df.java)
# print(reshaped_df.isna().values.any())
# print(type(pd.to_datetime(df.DATE[1])))

# %%
