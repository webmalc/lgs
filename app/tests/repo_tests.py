"""The configuration tests."""

from sqlmodel import Session, select

from app.dto.content import ContentRequestCreate
from app.models.content import ContentRequest
from app.repo.content import ContentRepository


def test_content_repository_create(session: Session) -> None:
    """Must create a content request."""
    assert not session.exec(select(ContentRequest)).first()
    repo = ContentRepository(session)
    content = "Test content to check"
    source = "test user profile"
    note = "test note"
    db_obj = repo.create(
        ContentRequestCreate(
            content=content,
            source=source,
            note=note,
        ))
    assert db_obj.id
    assert db_obj.score == 0
    assert db_obj.created_at
    assert db_obj.content == content
    assert db_obj.source == source
    assert db_obj.note == note


def test_content_repository_update_score(session: Session) -> None:
    """Must update a content request score."""
    repo = ContentRepository(session)
    content = "Test content to check"
    source = "test user profile"
    note = "test note"
    db_obj = repo.create(
        ContentRequestCreate(
            content=content,
            source=source,
            note=note,
        ))
    score = 50
    db_obj = repo.update_score(db_obj, score)
    assert db_obj.score == score
