from __future__ import annotations

from pydantic import Field

from src.shared.base_dto_models import BaseDepartmentDto, BaseDivisionDto, BaseCompanyDto


class GuiDepartmentDto(BaseDepartmentDto):
    pass


class GuiDivisionDto(BaseDivisionDto):
    departments: list[GuiDepartmentDto] = Field(default_factory=list)

class GuiCompanyDto(BaseCompanyDto):
    pass