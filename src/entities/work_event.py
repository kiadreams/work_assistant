from __future__ import annotations

from typing import TYPE_CHECKING

import datetime

from sqlalchemy import (
    ForeignKey,
    Date,
    Time,
    func,
)
from sqlalchemy.orm import (
    MappedAsDataclass,
    Mapped,
    mapped_column,
    relationship,
)

from ..databases.database import Base


if TYPE_CHECKING:
    from .work import Work
    from .employee import Employee


class WorkEvent(MappedAsDataclass, Base):
    __tablename__ = 'work_events'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    employee_service_number: Mapped[int] = mapped_column(ForeignKey('employees.service_number'), nullable=False)
    work_id: Mapped[int] = mapped_column(ForeignKey('works.id'), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False, server_default=func.now())

    work: Mapped[Work] = relationship(back_populates='events')
    employee: Mapped[Employee] = relationship(back_populates='work_events')

    start_time: Mapped[datetime.time] = mapped_column(Time, nullable=False, default=datetime.time(8, 30, 0))
    end_time: Mapped[datetime.time] = mapped_column(Time, nullable=False, default=datetime.time(16, 30, 0))
