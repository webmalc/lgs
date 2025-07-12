"""The configuration tests."""

from app.core.config import get_config


def test_get_config() -> None:
    assert get_config().api_key == "test_api_key"
