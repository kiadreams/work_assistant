from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

from src.core.models.division_domain import DivisionDomain
from src.infrastucture.database.db_manager import Base
from .company import Company
from ..dto import DbDivisionDto

if TYPE_CHECKING:
    from .department import Department
    from .employee_position import EmployeePosition


class Division(MappedAsDataclass, Base):
    __tablename__ = "divisions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    company: Mapped[Company] = relationship(back_populates="divisions", init=False)

    departments: Mapped[list[Department]] = relationship(
        back_populates="division", default_factory=list
    )
    employee_positions: Mapped[list[EmployeePosition]] = relationship(
        back_populates="division", default_factory=list
    )
    full_name: Mapped[str | None] = mapped_column(String(100), nullable=True, default=None)

    @classmethod
    def from_domain(cls, division: DbDivisionDto) -> Division:
        orm_division = cls(
            name=division.name,
            full_name=division.full_name,
            company_id=division.company_id,
        )
        return orm_division
