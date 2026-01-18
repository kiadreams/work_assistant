from __future__ import annotations

from pydantic import Field, field_validator

from src.shared.base_dto import BaseDepartmentDto, BaseDivisionDto


class DivisionDto(BaseDivisionDto):
    id: int | None = None
    departments: list[DepartmentDto] = Field(default_factory=list)

    @field_validator("name")
    @classmethod
    def name_validator(cls, name: str) -> str:
        if not name:
            raise ValueError("name must be a string and must not be empty")
        return name


class DepartmentDto(BaseDepartmentDto):
    id: int | None = None
