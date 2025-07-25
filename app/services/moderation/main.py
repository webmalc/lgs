"""The main moderation module."""

from app.dto.score import ContentScore

from .abstract import AbstractModerator
from .ai import AIModerator
from .stop_words import StopWordModerator


class Moderator:
    """The main moderator."""

    _code_mapper: dict[str, str] = {
        "ai": "ai",
        "stop_words": "stop_words",
    }

    moderators: list[AbstractModerator] = [AIModerator(), StopWordModerator()]

    def get_score(self, content: str) -> ContentScore:
        """Return the content moderation score 0-100. 0 - legal, 100-illegal."""
        return ContentScore(
            **{
                self._code_mapper[m.code]: m.get_score(content)
                for m in self.moderators
            })
