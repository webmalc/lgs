"""The stop words moderation module."""

import ahocorasick

from app.core.config import get_config

from .abstract import AbstractModerator


class StopWordModerator(AbstractModerator):
    """Moderator to check content with stop words."""

    automaton: ahocorasick.Automaton = None

    def __init__(self) -> None:
        if self.automaton:
            return
        conf = get_config()
        self.automaton = ahocorasick.Automaton()

        for idx, word in enumerate(conf.profane_words_en +
                                   conf.profane_words_ru):
            self.automaton.add_word(word, (idx, word))
        self.automaton.make_automaton()

    @property
    def code(self) -> str:
        return "stop_words"

    def get_score(self, content: str) -> int:
        return len(list(self.automaton.iter(content.lower()))) * 10
