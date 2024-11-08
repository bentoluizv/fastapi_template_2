from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
)

from hackathon.utils import generate_ulid_as_str


class Base(DeclarativeBase, MappedAsDataclass):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        init=False,
        default_factory=generate_ulid_as_str,
    )
    username: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, init=False, default_factory=func.now
    )
