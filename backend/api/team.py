from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Set
from analysis.team_anlaysis import get_all_team

router = APIRouter()


@router.get("/all-teams", tags=["team"])
def get_all_teams():
    all_teams: Set[str] = get_all_team()
    return JSONResponse(status_code=200, content=all_teams)
