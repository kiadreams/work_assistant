import datetime
from dataclasses import dataclass

from sqlalchemy import String, Date, ForeignKey, SmallInteger
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from src.packages.databases.engin_db import Base


@dataclass
class Department(MappedAsDataclass, Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True)

    employees: Mapped[list['Employee']] = relationship(back_populates='department')


@dataclass
class EmployeePosition(MappedAsDataclass, Base):
    __tablename__ = 'employee_positions'

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True)

    employees: Mapped[list['Employee']] = relationship(back_populates='employee_position')


@dataclass
class Employee(MappedAsDataclass, Base):
    __tablename__ = 'employees'

    service_number: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=False)
    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True)
    employee_position_id: Mapped[int] = mapped_column(ForeignKey('employee_positions.id'))
    department_id: Mapped[int] = mapped_column(ForeignKey('departments.id'))

    employee_position: Mapped[EmployeePosition] = relationship(back_populates='employees')
    department: Mapped[Department] = relationship(back_populates='employees')
