from __future__ import annotations

from pydantic import BaseModel, field_validator

from src.core.exceptions import StructureInvalidNameError


class BaseDivisionDto(BaseModel):
    id: int | None = None
    name: str
    full_name: str | None = None

    @field_validator("name")
    @classmethod
    def name_validator(cls, name: str) -> str:
        clean_name = name.strip()
        if not clean_name:
            raise StructureInvalidNameError("Не указано название службы...")
        return clean_name


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
