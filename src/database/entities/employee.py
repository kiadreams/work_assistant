from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Date,
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
    from .employee_position import EmployeePosition
    from .work_task import WorkTask


class Employee(MappedAsDataclass, Base):
    __tablename__ = "employees"

    service_number: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=False)
    employee_position_id: Mapped[int] = mapped_column(ForeignKey("employee_positions.id"))

    employee_position: Mapped[EmployeePosition] = relationship(back_populates="employees")
    work_tasks: Mapped[list[WorkTask]] = relationship(back_populates="employee")

    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True, default=None)
