"""The configuration tests."""

from sqlmodel import Session, select

from app.dto.content import ContentRequestCreate
from app.models.content import ContentRequest
from app.repo.content import ContentRepository


def test_content_repository_create(session: Session) -> None:
    """Must return the main router."""
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
        ),
    )
    assert db_obj.id
    assert db_obj.score == 0
    assert db_obj.created_at
    assert db_obj.content == content
    assert db_obj.source == source
    assert db_obj.note == note
