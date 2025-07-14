from fastapi import FastAPI

from app.api.routes.router import get_main_router

app = FastAPI()
app.include_router(get_main_router(), prefix="/api")
