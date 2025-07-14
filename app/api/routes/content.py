from fastapi import APIRouter

_router = APIRouter(prefix="/content", tags=["content"])


# TODO: test it
def get_content_router() -> APIRouter:
    """Return the content router."""
    return _router


# TODO: remove
@_router.get(
    "/",
)
def read_content() -> dict:
    return {"content": "test"}
