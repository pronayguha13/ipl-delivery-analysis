# import dependencies
import pandas as pd
import os

df = pd.read_csv("./analysis/deliveries.csv")


def cleanup():
    # read csv data
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

    file_path = "output/ipl-delivery-clean.csv"

    if os.path.exists(file_path):
        df.to_csv(file_path, mode="w", columns=df.columns)
    else:
        df.to_csv(file_path, mode="a", columns=df.columns)


def get_column_names():
    columns = df.columns.str.split("_").str.join(" ").str.title().tolist()
    return columns
