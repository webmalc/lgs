from fastapi import APIRouter

from app.api.deps import SessionDep
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
    db_obj = ContentRepository(session).create(content_in)
    db_obj.score = Moderator().get_score(db_obj.content).median
    return dto.ContentRequestPublic.model_validate(db_obj)
