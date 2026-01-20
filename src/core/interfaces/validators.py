from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from src.core.interfaces.services import EmployeeServiceProtocol
    from src.core.models.division_domain import DivisionDomain


class DivisionValidatorProtocol(Protocol):
    employee_service: EmployeeServiceProtocol

    def is_valid_division(self, division: DivisionDomain) -> bool: ...
