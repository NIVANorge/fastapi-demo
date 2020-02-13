from fastapi import FastAPI

from domain.observation import Observation
from validators import validate_observation

app = FastAPI(
    docs_url="/"
)


@app.get("/hello/{name}/age/{age}")
async def hello(name: str, age: int) -> str:
    return {
        "name": name,
        "age": age
    }


@app.post("/observation")
async def post_opservation(obs: Observation):
    return validate_observation(obs)
