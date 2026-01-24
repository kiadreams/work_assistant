from __future__ import annotations

from typing import TYPE_CHECKING

from src.core.exceptions import DivisionExistsError
from src.core.models.division_domain import DivisionDomain

if TYPE_CHECKING:
    from src.core.interfaces.data_protocols import DivisionDataProtocol
    from src.core.interfaces.services import EmployeeServiceProtocol


class DivisionValidator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service

    def create_division(self, division_dto: DivisionDataProtocol) -> DivisionDomain:
        division = DivisionDomain.division_from_data(division_dto)
        self._validate_business_rules(division)
        return division

    def _validate_business_rules(self, division: DivisionDomain) -> None:
        # all_division = self.employee_service.load_all_divisions()
        my_division = DivisionDomain(name="division.name", departments=[])
        all_division = [my_division]
        if any(division.name == d.name for d in all_division):
            raise DivisionExistsError("Данная служба уже существует...")
