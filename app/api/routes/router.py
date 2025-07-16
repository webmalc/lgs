from fastapi import APIRouter

from app.api.deps import AuthDep
from app.api.routes.content import get_content_router


def get_main_router() -> APIRouter:
    """Return the main router."""
    router = APIRouter(dependencies=[AuthDep])
    router.include_router(get_content_router())

    return router
