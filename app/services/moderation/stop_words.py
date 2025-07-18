"""The stop words moderation module."""

from .abstract import AbstractModerator


# TODO: test it
# TODO: implement
class StopWordModerator(AbstractModerator):
    """Moderator to check content with stop words."""

    @property
    def code(self) -> str:
        return "stop_words"

    def get_score(self, content: str) -> int:
        return 12
