from __future__ import annotations

from typing import Any

from src.core.interfaces.dto_protocols import DepartmentDtoProtocol


class DepartmentDomain:
    def __init__(
        self,
        *,
        name: str,
        division_id: int | None = None,
        full_name: str | None = None,
        department_id: int | None = None,
    ) -> None:
        self.id = department_id
        self.name = name
        self.division_id = division_id
        self.full_name = full_name

    @classmethod
    def department_from_data(cls, department_data: DepartmentDtoProtocol) -> DepartmentDomain:
        return cls(
            department_id=department_data.id,
            division_id=department_data.id,
            name=department_data.name,
            full_name=department_data.full_name,
        )

    @property
    def model_data(self) -> dict[str, Any]:
        return vars(self)
