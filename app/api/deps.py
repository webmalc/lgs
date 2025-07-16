from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from sqlmodel import Session

from app.core.config import get_config
from app.core.db import get_engine


def get_db() -> Generator[Session]:
    with Session(get_engine()) as session:
        yield session


def auth(x_token: Annotated[str | None, Header()] = None) -> None:
    if x_token != get_config().api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


SessionDep = Annotated[Session, Depends(get_db)]
AuthDep = Depends(auth)
