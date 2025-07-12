from fastapi import APIRouter, Path, HTTPException
from fastapi.responses import JSONResponse
from controller.bowler_controller import *

bowler_routes = APIRouter()


@bowler_routes.get("/bowlers/get-all-bowlers", tags=["bowlers"])
def get_all_bowler_for_all_teams_controller():
    bowlers_name = get_all_bowler_controller()
    return JSONResponse(status_code=200, content=bowlers_name)


@bowler_routes.get("/bowlers/get-bowlers/{team_name}", tags=["bowlers"])
def get_teamwise_bowlers(team_name: str = Path(..., description="Name of the team")):
    try:
        bowler_list: List[str] = get_teamwise_bowlers_analysis(team_name)
        return JSONResponse(status_code=200, content=bowler_list)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Team {team_name} not found")


@bowler_routes.get("/bowlers/stat", tags=["bowlers"])
def get_all_bowler_stat():
    get_all_bowler_stat_controller()
    return JSONResponse(status_code=200, content=[])
