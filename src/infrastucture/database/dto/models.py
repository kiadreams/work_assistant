from __future__ import annotations

from pydantic import ConfigDict, Field

from src.shared.base_dto import BaseDepartmentDto, BaseDivisionDto


class DepartmentDto(BaseDepartmentDto):
    model_config = ConfigDict(from_attributes=True)

    id: int


class DivisionDto(BaseDivisionDto):
    model_config = ConfigDict(from_attributes=True)

    id: int
    departments: list[DepartmentDto] = Field(default_factory=list)
