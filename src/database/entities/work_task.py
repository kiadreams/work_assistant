from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Date,
    ForeignKey,
    Time,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

from src.database.db_manager import Base

if TYPE_CHECKING:
    from .employee import Employee
    from .work import Work


class WorkTask(MappedAsDataclass, Base):
    __tablename__ = "work_tasks"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    employee_service_number: Mapped[int] = mapped_column(
        ForeignKey("employees.service_number"), nullable=False
    )
    work_id: Mapped[int] = mapped_column(ForeignKey("works.id"), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False, server_default=func.now())

    work: Mapped[Work] = relationship(back_populates="work_tasks")
    employee: Mapped[Employee] = relationship(back_populates="work_tasks")

    start_time: Mapped[datetime.time] = mapped_column(
        Time, nullable=False, default=datetime.time(8, 30, 0)
    )
    end_time: Mapped[datetime.time] = mapped_column(
        Time, nullable=False, default=datetime.time(16, 30, 0)
    )
