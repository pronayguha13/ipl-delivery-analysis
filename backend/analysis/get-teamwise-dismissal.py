#%%
import pandas as pd
import numpy as np
#%%
df = pd.read_csv("ipl-delivery-clean.csv")
#%%
df.drop(columns=["Unnamed: 0"], inplace=True)
#%%
df["batting_team"].unique()
#%%
df.groupby("batting_team")
#%%
