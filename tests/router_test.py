"""The configuration tests."""

from app.api.routes.router import get_content_router


def test_get_main_router() -> None:
    """Must return the main router."""
    assert get_content_router()
