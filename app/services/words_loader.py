"""The profane words loader."""

import csv
from pathlib import Path


def load_profane_words(lang: str = "en") -> list[str]:
    """Loads the profane words."""

    with Path(f"app/data/{lang}_profane_words.txt").open("r") as read_obj:
        return [r[0] for r in csv.reader(read_obj) if r]
