import datetime
from dataclasses import dataclass

from sqlalchemy import String, Date, Enum
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column

from src.packages.databases.engin_db import Base
from types_of_value import EmployeePosition


@dataclass
class Employee(MappedAsDataclass, Base):
    __tablename__ = 'employees'

    service_number: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=False)
    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True)
    employee_position: Mapped[EmployeePosition] = mapped_column(Enum(EmployeePosition), nullable=False)
