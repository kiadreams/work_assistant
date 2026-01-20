from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.interfaces.services import EmployeeServiceProtocol
    from core.models.division_domain import DivisionDomain


class DivisionValidator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service

    def is_valid_division(self, division: DivisionDomain) -> bool:
        all_division = self.employee_service.load_all_divisions()
        return any(division.name == d.name for d in all_division)
