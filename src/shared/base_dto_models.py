from __future__ import annotations

from typing import Sequence

from pydantic import BaseModel, Field, field_validator

from src.core.exceptions.business_exceptions import StructureInvalidNameError
from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain


class BaseDivisionDto(BaseModel):
    id: int | None = None
    name: str
    full_name: str | None = None
    departments: Sequence[BaseDepartmentDto] = Field(default_factory=list)

    @field_validator("name")
    @classmethod
    def name_validator(cls, name: str) -> str:
        clean_name = name.strip()
        if not clean_name:
            raise StructureInvalidNameError("Не указано название службы...")
        return clean_name

    def to_domain(self) -> DivisionDomain:
        departments = [d.to_domain() for d in self.departments] if self.departments else []
        division = DivisionDomain(
            division_id=self.id,
            name=self.name,
            full_name=self.full_name,
            departments=departments,
        )
        return division


class BaseDepartmentDto(BaseModel):
    id: int | None = None
    name: str
    division_id: int | None = None
    full_name: str | None = None

    @field_validator("name")
    @classmethod
    def name_validator(cls, name: str) -> str:
        clean_name = name.strip()
        if not clean_name:
            raise StructureInvalidNameError("Название отдела не содержит символов...")
        return clean_name

    def to_domain(self) -> DepartmentDomain:
        department = DepartmentDomain(
            department_id=self.id,
            name=self.name,
            full_name=self.full_name,
            division_id=self.division_id,
        )
        return department
