"""The ai moderation module."""

from .abstract import AbstractModerator


# TODO: test it
# TODO: implement
class AIModerator(AbstractModerator):
    """Moderator to check content with AI."""

    @property
    def code(self) -> str:
        return "ai"

    def get_score(self, content: str) -> int:
        return 43
