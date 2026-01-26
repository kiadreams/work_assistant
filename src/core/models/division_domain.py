from __future__ import annotations

from typing import TYPE_CHECKING, Any

from src.core.models.department_domain import DepartmentDomain

if TYPE_CHECKING:
    from src.core.interfaces.dto_protocols import DepartmentDtoProtocol, DivisionDtoProtocol


class DivisionDomain:
    def __init__(
        self,
        *,
        name: str,
        full_name: str | None = None,
        departments: list[DepartmentDomain],
        division_id: int | None = None,
    ) -> None:
        self.id = division_id
        self.name = name
        self.full_name = full_name
        self.departments = departments

    @classmethod
    def division_from_data(cls, division_data: DivisionDtoProtocol) -> DivisionDomain:
        departments_data: list[DepartmentDtoProtocol] = division_data.departments
        departments = []
        if departments_data:
            departments = [DepartmentDomain.model_validate(d) for d in departments_data]
        return cls(
            division_id=division_data.id,
            name=division_data.name,
            full_name=division_data.full_name,
            departments=departments,
        )

    @property
    def model_data(self) -> dict[str, Any]:
        division_data = {}
        for name, value in vars(self).items():
            if isinstance(value, list):
                value = [e.model_data for e in value]
            division_data[name] = value
        return division_data
