"""The configuration tests."""

from datetime import date

from sqlmodel import text

from app.core.db import get_engine


def test_engine() -> None:
    engine = get_engine()
    with engine.connect() as connection:
        result = connection.execute(text("SELECT NOW()::DATE;"))
        assert result.one()[0] == date.today()
