"""The configuration tests."""

from app.core.logging import get_logger


def test_get_logger() -> None:
    assert get_logger()
