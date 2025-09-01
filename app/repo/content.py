"""The content repository."""

from dataclasses import dataclass

from sqlmodel import Session

from app.dto.content import ContentRequestCreate
from app.models.content import ContentRequest


@dataclass
class ContentRepository:
    session: Session

    def create(self, content_in: ContentRequestCreate) -> ContentRequest:
        """Create the obj."""
        db_obj = ContentRequest.model_validate(
            content_in.model_dump(exclude_unset=True))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)

        return db_obj

    def update_score(
        self,
        content: ContentRequest,
        score: int,
    ) -> ContentRequest:
        """Update the obj."""
        content.sqlmodel_update({"score": score})
        self.session.add(content)
        self.session.commit()
        self.session.refresh(content)

        return content
