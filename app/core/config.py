"""The main configuration module."""

from functools import cache
from os import getenv

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.services.words_loader import load_profane_words


class Settings(BaseSettings):
    """The base settings class."""

    model_config = SettingsConfigDict(
        env_prefix="lgs_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    is_prod: bool = False
    api_key: str = ""
    database_url: str = ""
    sentry_dsn: str = ""
    profane_words_ru: list[str] = []
    profane_words_en: list[str] = []


def _load_profane_words_to_conf(conf: Settings) -> None:
    """Load profane words to the config."""
    for lang in ["en", "ru"]:
        if not getattr(conf, f"profane_words_{lang}"):
            setattr(conf, f"profane_words_{lang}", load_profane_words(lang))


@cache
def get_config() -> Settings:
    """Returns settings."""
    if getenv("LGS_TESTS"):
        conf = Settings(_env_file="app/tests/test.env")  # type: ignore
    else:
        conf = Settings(_env_file="prod.env")  # type: ignore
    _load_profane_words_to_conf(conf)

    return conf
