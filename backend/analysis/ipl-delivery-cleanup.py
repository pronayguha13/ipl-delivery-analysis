# import dependencies
import pandas as pd
import numpy as np

# read csv data
df = pd.read_csv("deliveries.csv")
df.head()
df.info()
df["is_super_over"].unique()
df["player_dismissed"] = df["player_dismissed"].fillna("")
df["dismissal_kind"] = df["dismissal_kind"].fillna("")
df["fielder"] = df["fielder"].fillna("")
df["inning"] = df["inning"].astype("int8")
df["batting_team"] = df["batting_team"].astype("category")
df["bowling_team"] = df["bowling_team"].astype("category")
df["is_super_over"] = df["is_super_over"].astype("bool")
df["ball"] = df["ball"].astype("int8")
df["over"] = df["over"].astype("int8")
df.info()
import os

if os.path.exists("ipl-delivery-clean.csv"):
    df.to_csv("ipl-delivery-clean.csv", mode="w", columns=df.columns)
else:
    df.to_csv("ipl-delivery-clean.csv", mode="a", columns=df.columns)
# %%
