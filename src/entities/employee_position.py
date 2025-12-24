from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import (
    MappedAsDataclass,
    Mapped,
    mapped_column,
    relationship,
)

from ..databases.database import Base


if TYPE_CHECKING:
    from .division import Division
    from .department import Department
    from .employee import Employee


class EmployeePosition(MappedAsDataclass, Base):
    __tablename__ = "employee_positions"

    __table_args__ = (
        CheckConstraint(
            sqltext="(division_id IS NOT NULL AND department_id IS NULL) "
            "OR (division_id IS NULL AND department_id IS NOT NULL)",
            name="chk_single_department",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    division_id: Mapped[int] = mapped_column(ForeignKey("divisions.id"))
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))

    division: Mapped[Division] = relationship(back_populates="employee_positions", default=None)
    department: Mapped[Department] = relationship(back_populates="employee_positions", default=None)
    employees: Mapped[list[Employee]] = relationship(
        back_populates="employee_position", default_factory=list
    )

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
