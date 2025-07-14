"""The database models."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Text, func
from sqlmodel import Field, SQLModel


class ContentRequest(SQLModel):
    """The content request to check."""

    content: str = Field(sa_column=Column(Text))  # long text field
    source: str
    note: str | None = None
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            default=func.now(),
            nullable=False,
        ),
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
    )
    score: int = Field(
        default=0,
        description="Score of the text. 0 - acceptable, 100-inappropriate",
    )
