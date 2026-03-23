from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

from src.infrastucture.database.db_manager import Base

if TYPE_CHECKING:
    from .division import Division


class Company(MappedAsDataclass, Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    divisions: Mapped[list[Division]] = relationship(back_populates="company", default_factory=list)
    full_name: Mapped[str | None] = mapped_column(String(100), nullable=True, default=None)
