"""The main configuration module."""

from functools import cache
from os import getenv

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """The base settings class."""

    model_config = SettingsConfigDict(
        env_prefix="lgs_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    api_key: str = ""
    database_url: str = ""


@cache
def get_config() -> Settings:
    """Returns settings."""
    if getenv("LGS_TESTS"):
        return Settings(_env_file="app/tests/test.env")
    return Settings()
