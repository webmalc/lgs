"""The ai moderation module."""

from .abstract import AbstractModerator


class AIModerator(AbstractModerator):
    """Moderator to check content with AI."""

    @property
    def code(self) -> str:
        return "ai"

    def get_score(self, _: str) -> int:
        return 0
