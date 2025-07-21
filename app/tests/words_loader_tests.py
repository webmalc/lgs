"""The configuration tests."""

from app.services.words_loader import load_profane_words


def test_load_profane_words() -> None:
    words = load_profane_words("en")
    assert "ass" in words
    assert "slut" in words

    words = load_profane_words("ru")
    assert "анус" in words
    assert "ялд" in words
