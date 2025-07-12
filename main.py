from fastapi import FastAPI

from app.core.config import get_config

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"Hello": get_config().api_key}
