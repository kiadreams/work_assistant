import datetime

from sqlalchemy import String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from . import works
from ..databases.database import Base

class Service(MappedAsDataclass, Base):
    __tablename__ = 'services'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    departments: Mapped[list['Employee']] = relationship(back_populates='service')
    employee_positions: Mapped[list['EmployeePosition']] = relationship(back_populates='service')

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class Department(MappedAsDataclass, Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))

    service: Mapped['Service'] = relationship(back_populates='departments')
    employee_positions: Mapped[list['EmployeePosition']] = relationship(back_populates='department')

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class EmployeePosition(MappedAsDataclass, Base):
    __tablename__ = 'employee_positions'

    __table_args__ = (
        CheckConstraint(
            sqltext='(service_id IS NOT NULL AND department_id IS NULL) '
                    'OR (service_id IS NULL AND department_id IS NOT NULL)',
            name='chk_single_department'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))
    department_id: Mapped[int] = mapped_column(ForeignKey('departments.id'))

    service: Mapped['Service'] = relationship(back_populates='employee_positions')
    department: Mapped['Department'] = relationship(back_populates='employee_positions')
    employees: Mapped[list['Employee']] = relationship(back_populates='employee_position')

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class Employee(MappedAsDataclass, Base):
    __tablename__ = 'employees'

    service_number: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=False)
    employee_position_id: Mapped[int] = mapped_column(ForeignKey('employee_positions.id'))

    employee_position: Mapped['EmployeePosition'] = relationship(back_populates='employees')
    work_event: Mapped['works.WorkEvent'] = relationship(back_populates='employee')

    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True, default=None)
