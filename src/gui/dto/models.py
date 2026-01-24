from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field, field_validator

from src.shared.base_dto import BaseDepartmentDto, BaseDivisionDto

if TYPE_CHECKING:
    from src.core.interfaces.data_protocols import DepartmentDataProtocol


class DivisionDto(BaseDivisionDto):
    id: int | None = None
    departments: list[DepartmentDataProtocol] = Field(default_factory=list)

    @field_validator("name")
    @classmethod
    def name_validator(cls, name: str) -> str:
        if not name:
            raise ValueError("name must be a string and must not be empty")
        return name


class DepartmentDto(BaseDepartmentDto):
    id: int | None = None
