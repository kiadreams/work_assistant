from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from src.core.models.department_domain import DepartmentDomain

if TYPE_CHECKING:
    from src.core.models.division_domain import DivisionDomain


class DivisionRepositoryProtocol(Protocol):
    @property
    def all_divisions(self) -> list[DivisionDomain]: ...

    def add_new_division(self, division: DivisionDomain) -> DivisionDomain: ...

    def add_new_department(self, department: DepartmentDomain) -> DepartmentDomain: ...

    def edit_division_by_id(self, division_id: int, division: DivisionDomain) -> DivisionDomain: ...

    def edit_department_by_id(
        self, department_id: int, department: DepartmentDomain
    ) -> DepartmentDomain: ...

    def delete_division_by_id(self, division_id: int) -> None: ...

    def delete_department_by_id(self, department_id: int) -> None: ...
