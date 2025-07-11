from fastapi.responses import JSONResponse
from analysis.bowler_analysis import *


def get_all_bowler_controller():
    response = get_all_bowler_analysis()
    return response


def get_teamwise_all_bowler_controller(team_name: str):
    response = get_teamwise_bowlers_analysis(team_name)
    return response
