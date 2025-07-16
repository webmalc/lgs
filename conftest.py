"""Tests fixtures module."""

import os
from collections.abc import Generator
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import MetaData
from sqlmodel import Session

from app.core.config import get_config
from app.core.db import get_engine
from main import app


@pytest.fixture(scope="session", autouse=True)
def set_env() -> None:
    os.environ["LGS_TESTS"] = "1"


@pytest.fixture
def client_without_token() -> TestClient:
    return TestClient(app)


@pytest.fixture
def client(client_without_token: TestClient) -> TestClient:
    client_without_token.headers = {"X-token": get_config().api_key}
    return client_without_token


@pytest.fixture
def session() -> Generator[Session]:
    """Return DB session."""
    # drop database
    engine = get_engine()
    assert str(engine.url).endswith("_test")
    metadata = MetaData()
    metadata.reflect(bind=engine, schema="public")
    metadata.drop_all(bind=engine)

    # run migrations
    alembic_cfg = Config(Path(__file__).resolve().parent / "alembic.ini")
    command.upgrade(alembic_cfg, "head")

    # provide session
    with Session(engine) as session:
        yield session
