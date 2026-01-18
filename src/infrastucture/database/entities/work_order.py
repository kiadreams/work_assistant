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
    from .work import Work


class WorkOrder(MappedAsDataclass, Base):
    __tablename__ = "work_orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)

    works: Mapped[list[Work]] = relationship(back_populates="work_order")

    number: Mapped[str] = mapped_column(String(20), nullable=False, default="V05110______")
