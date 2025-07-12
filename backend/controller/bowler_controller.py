from fastapi.responses import JSONResponse
from analysis.bowler_analysis import *


def get_all_bowler_controller():
    response = get_all_bowler_analysis()
    return response


def get_teamwise_all_bowler_controller(team_name: str):
    response = get_teamwise_bowlers_analysis(team_name)
    return response


def get_bowler_stat_controller(bowler_name: str):
    print(f"Received request to serve the stat of the bowler named: {bowler_name}")
    get_bowler_stat_analysis(bowler_name)


#
def get_all_bowler_stat_controller():
    all_bowler = get_all_bowler_controller()
    for _, bowlers in all_bowler.items():
        for bowler in bowlers:
            print(f"fetching stat of : {bowler}")
            get_bowler_stat_controller(bowler)
