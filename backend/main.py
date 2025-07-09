from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# init app
app = FastAPI()

# setup cors
origins = [
    "http://localhost:3000",
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"], )


@app.get("/")
def root():
    return JSONResponse({"message": "Root Page"})
