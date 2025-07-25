"""The stop words tests."""

from app.services.moderation.main import Moderator


def test_main_moderator_get_score() -> None:
    """Must detect profane words."""
    moderator = Moderator()
    score = moderator.get_score("ass foo bar slut foo bar")
    assert score.stop_words == 20
    assert score.ai == 0
