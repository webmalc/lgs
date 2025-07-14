from fastapi import APIRouter

from app.api.routes.content import get_content_router


# TODO: test it
def get_main_router() -> APIRouter:
    """Return the main router."""
    router = APIRouter()
    router.include_router(get_content_router())

    return router
