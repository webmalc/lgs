"""The main db module."""

from functools import cache

from sqlalchemy import Engine
from sqlmodel import create_engine

from app.core.config import get_config
from app.models.db import *  # noqa: F403


@cache
def get_engine() -> Engine:
    """Return the main engine."""
    return create_engine(get_config().database_url)
