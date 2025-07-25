"""The content score."""

from dataclasses import dataclass
from statistics import median


@dataclass
class ContentScore:
    """The content score by services."""

    stop_words: int
    ai: int

    STOP_WORDS_RATIO: float = 1
    AI_RATIO: float = 1.5

    @property
    def median(self) -> int:
        """Return the median result."""
        return min(
            round(
                median([
                    self.stop_words * self.STOP_WORDS_RATIO,
                    self.ai * self.AI_RATIO,
                ])),
            100,
        )
