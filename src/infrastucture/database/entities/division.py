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
    from .department import Department
    from .employee_position import EmployeePosition


class Division(MappedAsDataclass, Base):
    __tablename__ = "divisions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    departments: Mapped[list[Department]] = relationship(
        back_populates="division", default_factory=list
    )
    employee_positions: Mapped[list[EmployeePosition]] = relationship(
        back_populates="division", default_factory=list
    )

    full_name: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
