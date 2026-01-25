from __future__ import annotations

from pydantic import ConfigDict, Field

from src.shared.base_dto_models import BaseDepartmentDto, BaseDivisionDto


class DbDepartmentDto(BaseDepartmentDto):
    model_config = ConfigDict(from_attributes=True)


class DbDivisionDto(BaseDivisionDto):
    model_config = ConfigDict(from_attributes=True)

    departments: list[DbDepartmentDto] = Field(default_factory=list)
