from __future__ import annotations

from typing import Any

from src.core.models.department_domain import DepartmentDomain


class DivisionDomain:
    def __init__(
        self,
        *,
        division_id: int | None = None,
        name: str,
        full_name: str | None = None,
        departments: list[DepartmentDomain],
    ) -> None:
        self.id = division_id
        self.name = name
        self.full_name = full_name
        self.departments = departments

    @property
    def model_data(self) -> dict[str, Any]:
        division_data = {}
        for name, value in vars(self).items():
            if isinstance(value, list):
                value = [e.model_data for e in value]
            division_data[name] = value
        return division_data
