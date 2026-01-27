from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from src.core.models.department_domain import DepartmentDomain

if TYPE_CHECKING:
    from src.core.models.division_domain import DivisionDomain


class EmployeeServiceProtocol(Protocol):
    def load_all_divisions(self) -> list[DivisionDomain]: ...

    def add_new_division(self, division: DivisionDomain) -> DivisionDomain: ...

    def edit_division_data_by_id(
        self, division_id: int, division: DivisionDomain
    ) -> DivisionDomain: ...

    def delete_division_by_id(self, division_id: int) -> None: ...

    def add_new_department(self, department: DepartmentDomain) -> DepartmentDomain: ...

    def edit_department_data_by_id(
        self, department_id: int, department: DepartmentDomain
    ) -> DepartmentDomain: ...

    def delete_department_by_id(self, department_id: int) -> None: ...
