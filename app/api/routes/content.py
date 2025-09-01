from fastapi import APIRouter

from app.api.deps import SessionDep
from app.core.logging import get_logger
from app.dto import content as dto
from app.repo.content import ContentRepository
from app.services.moderation import Moderator

_router = APIRouter(prefix="/content", tags=["content"])


def get_content_router() -> APIRouter:
    """Return the content router."""
    return _router


@_router.post("/", response_model=dto.ContentRequestPublic)
def create_content_request(
    *,
    session: SessionDep,
    content_in: dto.ContentRequestCreate,
) -> dto.ContentRequestPublic:
    get_logger().info("Creating content request: %s", content_in)
    db_obj = ContentRepository(session).create(content_in)
    score = Moderator().get_score(db_obj.content).median
    get_logger().info(
        "Saving score for content request: %s. Score: %s",
        content_in,
        score,
    )
    ContentRepository(session).update_score(db_obj, score)
    return dto.ContentRequestPublic.model_validate(db_obj)
