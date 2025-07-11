import pandas as pd

df = pd.read_csv("./output/ipl-delivery-clean.csv")


def get_all_team():
    bowling_team = df["bowling_team"].unique().tolist()
    batting_team = df["batting_team"].unique().tolist()

    all_teams = list(set(bowling_team + batting_team))
    return all_teams

