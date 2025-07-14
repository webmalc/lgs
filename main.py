from fastapi import FastAPI

from app.core.config import get_config
from app.core.logging import get_logger

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    get_logger().info("test info")

    return {"Hello": get_config().database_url}
