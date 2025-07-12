"""Tests fixtures module."""

import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def set_env() -> None:
    os.environ["LGS_TESTS"] = "1"
