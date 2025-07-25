"""The stop words tests."""

from app.services.moderation.stop_words import StopWordModerator


def test_stop_words_get_score() -> None:
    """Must detect profane words."""
    moderator = StopWordModerator()
    assert moderator.get_score("ass foo bar") == 10
    assert moderator.get_score("ass foo bar slut") == 20
    assert moderator.get_score("ass foo bar ass") == 20
    assert moderator.get_score("ass foo bar profane_one_ru") == 20
