from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from typing import List
from analysis.bowler_analysis import (get_all_bowler_for_all_teams,
                                      get_teamwise_bowlers_controller)

router = APIRouter()


@router.get("/get-all-bowler-for-all-teams")
def get_all_bowler_for_all_teams_controller():
    bowlers_name = get_all_bowler_for_all_teams()
    return JSONResponse(status_code=200, content=bowlers_name)


@router.get("/get-bowlers/{team_name}")
def get_teamwise_bowlers(team_name: str = Path(..., description="Name of the team")):
    bowler_list: List[str] = get_teamwise_bowlers_controller(team_name)
    return JSONResponse(status_code=200, content=bowler_list)
