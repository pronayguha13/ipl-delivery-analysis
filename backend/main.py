from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from analysis.ipl_delivery_cleanup import cleanup, get_column_names
from api.bowler import bowler_routes
from api.team import router as team_analysis_routes

# init app
app = FastAPI()

# setup cors
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return JSONResponse({"message": "Root Page"})


@app.get("/cleanup")
def cleanup_view():
    cleanup()
    return JSONResponse(status_code=201, content={})


@app.get("/columns")
def get_column_names_controller():
    columns = get_column_names()
    return JSONResponse(status_code=200, content=columns)


app.include_router(bowler_routes)
app.include_router(team_analysis_routes)
