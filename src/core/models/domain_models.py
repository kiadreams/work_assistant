from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class DivisionDomain(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    full_name: str | None
    departments: list[DepartmentDomain] = []


class DepartmentDomain(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    full_name: str | None
    division_id: int
