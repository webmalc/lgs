from pydantic import Field
from sqlmodel import SQLModel

from app.models.content import ContentRequestBase


class ContentRequestCreate(SQLModel):
    """The DTO the create content request."""

    content: str = Field(title="The text to check.", min_length=10)
    source: str = Field(
        title="The source of text. E.g. user profile, order description.",
        min_length=3,
        max_length=255,
    )
    note: str = Field(
        title="The some arbitrary system information.",
        min_length=3,
    )


class ContentRequestPublic(ContentRequestBase):
    """The the DTO list content request."""
