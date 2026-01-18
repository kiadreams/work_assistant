from __future__ import annotations

from pydantic import BaseModel


class BaseDivisionDto(BaseModel):
    name: str
    full_name: str | None = None


class BaseDepartmentDto(BaseModel):
    name: str
    full_name: str | None = None
    division_id: int | None = None
