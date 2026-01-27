from __future__ import annotations

from typing import TYPE_CHECKING

from src.core.exceptions.business_exceptions import StructureExistsError
from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain

if TYPE_CHECKING:
    from src.core.interfaces.services import EmployeeServiceProtocol
    from src.gui.dto.gui_dto_models import GuiDepartmentDto, GuiDivisionDto


class DivisionValidator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service

    def create_division(self, division_dto: GuiDivisionDto) -> DivisionDomain:
        division = division_dto.to_domain()
        self._validate_business_rules(division)
        return division

    def _validate_business_rules(self, division: DivisionDomain) -> None:
        # all_division = self.employee_service.load_all_divisions()
        my_division = DivisionDomain(name="division.name", departments=[])
        all_division = [my_division]
        if any(division.name == d.name for d in all_division):
            raise StructureExistsError("Данная служба уже существует...")


class DepartmentValidator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service

    def create_department(self, department_dto: GuiDepartmentDto) -> DepartmentDomain:
        department = department_dto.to_domain()
        self._validate_business_rules(department)
        return department

    def _validate_business_rules(self, department: DepartmentDomain) -> None:
        # all_division = self.employee_service.load_all_divisions()
        my_department = DepartmentDomain(name="department.name")
        all_department = [my_department]
        if any(department.name == d.name for d in all_department):
            raise StructureExistsError("Данная служба уже существует...")
