import datetime

from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from src.databases import Base
from . import work_db_tables


class Employee(MappedAsDataclass, Base):
    __tablename__ = 'employees'

    service_number: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=False)
    employee_position_id: Mapped[int] = mapped_column(ForeignKey('employee_positions.id'))

    employee_position: Mapped['EmployeePosition'] = relationship(back_populates='employees')
    work_events: Mapped[list['work_db_tables.WorkEvent']] = relationship(back_populates='employee')

    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True, default=None)
