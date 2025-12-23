from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    ForeignKey,
    Date,
)
from sqlalchemy.orm import (
    MappedAsDataclass,
    Mapped,
    mapped_column,
    relationship,
)

from ..databases.database import Base


if TYPE_CHECKING:
    from .employee_position import EmployeePosition
    from .work_event import WorkEvent


class Employee(MappedAsDataclass, Base):
    __tablename__ = 'employees'

    service_number: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=False)
    employee_position_id: Mapped[int] = mapped_column(ForeignKey('employee_positions.id'))

    employee_position: Mapped[EmployeePosition] = relationship(back_populates='employees')
    work_events: Mapped[list[WorkEvent]] = relationship(back_populates='employee')

    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True, default=None)
