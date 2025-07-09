import pandas as pd
from typing import List

df = pd.read_csv("./output/ipl-delivery-clean.csv")

team_group = df.groupby("bowling_team")

bowling_team = df["bowling_team"].unique()


def get_all_bowler_for_all_teams():
    bowler_list = {}
    for team in bowling_team:
        bowler_team = team_group.get_group(team)
        bowler = bowler_team["bowler"].unique().tolist()
        bowler_list[team] = bowler
    return bowler_list


def get_teamwise_bowlers_controller(team_name: str) -> List[str]:
    team = team_group.get_group(team_name)
    bowlers = team["bowler"].unique().tolist()
    return bowlers
