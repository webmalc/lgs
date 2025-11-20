"""The configuration tests."""

from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.core.config import get_config
from app.models.content import ContentRequest


def test_create_content_request_route_unauth(client_without_token: TestClient) -> None:
    """Must throw 401 exception."""
    response = client_without_token.post("/api/content/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = client_without_token.get(
        "/items/foo",
        headers={"X-Token": get_config().api_key},
    )
    assert response.status_code != status.HTTP_401_UNAUTHORIZED


def test_create_content_request_route(client: TestClient, session: Session) -> None:
    """Must create a content request."""
    assert not session.exec(select(ContentRequest)).first()
    content = "some content to check"
    source = "user info"
    note = "some note"
    response = client.post(
        "/api/content/",
        json={
            "content": content,
            "source": source,
            "note": note,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["content"] == content
    assert data["source"] == source
    assert data["note"] == note

    db_obj = session.exec(select(ContentRequest)).first()
    assert db_obj
    assert db_obj.id
    assert db_obj.created_at
    assert db_obj.content == content
    assert db_obj.source == source
    assert db_obj.note == note
