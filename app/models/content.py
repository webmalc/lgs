"""The database models."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Text, func
from sqlmodel import Field, SQLModel


class ContentRequestBase(SQLModel):
    """The content request base fields."""

    id: int = Field(default=None, primary_key=True)
    content: str = Field(sa_column=Column(Text))  # long text field
    score: int = Field(
        default=0,
        ge=0,
        le=100,
        description="Score of the text. 0 - acceptable, 100-inappropriate",
    )
    source: str
    note: str | None = None


class ContentRequest(ContentRequestBase, table=True):
    """The content request to check."""

    created_at: datetime = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            default=func.now(),
            nullable=False,
        ),
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
    )
