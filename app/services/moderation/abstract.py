"""The main moderation module."""

from abc import ABC, abstractmethod


class AbstractModerator(ABC):
    """The abstract moderator class."""

    @abstractmethod
    def get_score(self, content: str) -> int:
        """Get score 0-100. 0 - legal, 100-illegal."""

    @property
    @abstractmethod
    def code(self) -> str:
        """Get moderator code."""
