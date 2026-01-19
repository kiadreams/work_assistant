from __future__ import annotations

from typing import TYPE_CHECKING

from core.models.department_domain import DepartmentDomain

if TYPE_CHECKING:
    from core.interfaces.data_protocols import DepartmentDataProtocol, DivisionDataProtocol


class DivisionDomain:
    def __init__(
        self,
        *,
        name: str,
        full_name: str | None = None,
        departments: list[DepartmentDomain],
        division_id: int | None = None,
    ) -> None:
        self._id = division_id
        self._name = name
        self._full_name = full_name
        self._departments = departments

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def full_name(self) -> str | None:
        return self._full_name

    @property
    def departments(self) -> list[DepartmentDomain]:
        return self._departments

    @classmethod
    def division_from_data(cls, division_data: DivisionDataProtocol) -> DivisionDomain:
        departments_data: list[DepartmentDataProtocol] = division_data.departments
        departments = []
        if departments_data:
            departments = [DepartmentDomain.model_validate(d) for d in departments_data]
        return cls(
            division_id=division_data.id,
            name=division_data.name,
            full_name=division_data.full_name,
            departments=departments,
        )
