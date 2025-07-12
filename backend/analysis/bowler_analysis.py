import pandas as pd
from typing import List
from analysis.team_anlaysis import get_all_team

df = pd.read_csv("./output/ipl-delivery-clean.csv")

team_group = df.groupby("bowling_team")

bowling_team = df["bowling_team"].unique()


def get_all_bowler_analysis():
    bowler_list = {}
    for team in bowling_team:
        bowler_team = team_group.get_group(team)
        bowler = bowler_team["bowler"].unique().tolist()
        bowler_list[team] = bowler
    return bowler_list


def get_teamwise_bowlers_analysis(team_name: str) -> List[str]:
    all_teams = get_all_team()
    if team_name not in all_teams:
        raise KeyError(f"{team_name} is not present in the team list")
    team = team_group.get_group(team_name)
    bowlers = team["bowler"].unique().tolist()
    return bowlers


def get_bowler_stat_analysis(bowler_name):
    bowlers_group = df.groupby("bowler")
    bowler_data = bowlers_group.get_group(bowler_name)
    print(bowler_data)
