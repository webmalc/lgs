"""The score tests."""

from app.dto.score import ContentScore


def test_content_score_median() -> None:
    """Must return the median score."""
    assert ContentScore(
        stop_words=0,
        ai=0,
    ).median == 0

    assert ContentScore(
        stop_words=50,
        ai=0,
    ).median == 25

    assert ContentScore(
        stop_words=50,
        ai=50,
    ).median == 62

    assert ContentScore(
        stop_words=75,
        ai=50,
    ).median == 75
