"""The main logging module."""

import logging
from functools import cache

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | "
    "%(process)d >>> %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@cache
def get_logger() -> logging.Logger:
    """Return the main logger."""
    return logging.getLogger("main")
