from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from calc import calc_execute
from calc.customerr import CalcException
from .model import Command


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return FileResponse("website/index.html")


@app.get("/style")
def style():
    return FileResponse("website/style.css")


@app.get("/script")
def script():
    return FileResponse("website/script.js")


@app.get("/heath")
def health():
    return "Healthy"


@app.post("/execute")
def execute(_command: Command, response: Response):
    try:
        res = calc_execute(_command.command)
    except CalcException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "Error": e
        }
    return {
        "command": _command.command,
        "result": res
    }

