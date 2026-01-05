from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

from src.database.db_manager import Base

if TYPE_CHECKING:
    from .division import Division
    from .employee_position import EmployeePosition


class Department(MappedAsDataclass, Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    division_id: Mapped[int] = mapped_column(ForeignKey("divisions.id"))

    division: Mapped[Division] = relationship(back_populates="departments")
    employee_positions: Mapped[list[EmployeePosition]] = relationship(
        back_populates="department", default_factory=list
    )
    full_name: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
