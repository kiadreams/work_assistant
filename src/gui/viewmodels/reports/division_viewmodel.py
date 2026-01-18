from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import QObject, Signal

from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain

if TYPE_CHECKING:
    from core.interfaces.services import EmployeeServiceProtocol


class DivisionViewModel(QObject):
    division_data_changed_signal = Signal()
    department_data_changed_signal = Signal()

    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        super().__init__()
        self._employee_service = employee_service
        self.__divisions: list[DivisionDomain] = []
        self.__current_division: DivisionDomain | None = None
        self.__departments: list[DepartmentDomain] = []
        self.__current_department: DepartmentDomain | None = None

    def init_model_data(self) -> None:
        self.load_all_divisions()

    @property
    def divisions(self) -> list[DivisionDomain]:
        return self.__divisions

    @divisions.setter
    def divisions(self, value: list[DivisionDomain]) -> None:
        self.__divisions = value
        self.current_division = value[0] if value else None

    @property
    def current_division(self) -> DivisionDomain | None:
        return self.__current_division

    @current_division.setter
    def current_division(self, division: DivisionDomain | None) -> None:
        self.__current_division = division
        self.departments = division.departments if division else []
        self.division_data_changed_signal.emit()

    @property
    def departments(self) -> list[DepartmentDomain]:
        return self.__departments

    @departments.setter
    def departments(self, value: list[DepartmentDomain]) -> None:
        self.__departments = value
        self.current_department = value[0] if value else None

    @property
    def current_department(self) -> DepartmentDomain | None:
        return self.__current_department

    @current_department.setter
    def current_department(self, department: DepartmentDomain | None) -> None:
        self.__current_department = department
        self.department_data_changed_signal.emit()

    @property
    def can_delete_current_division(self) -> bool:
        if self.current_division:
            return True
        return False

    @property
    def can_edit_current_division(self) -> bool:
        if self.current_division:
            return True
        return False

    @property
    def can_show_all_divisions(self) -> bool:
        if self.divisions:
            return True
        return False

    @property
    def can_delete_current_department(self) -> bool:
        if self.current_department:
            return True
        return False

    @property
    def can_edit_current_department(self) -> bool:
        if self.current_department:
            return True
        return False

    @property
    def can_show_departments_of_division(self) -> bool:
        if self.departments:
            return True
        return False

    @property
    def division_name_data(self) -> tuple[list[str | None], str | None]:
        division_names = [d.name for d in self.divisions] if self.divisions else []
        current_division_name = self.current_division.name if self.current_division else ""
        return division_names, current_division_name

    @property
    def department_name_data(self) -> tuple[list[str], str]:
        department_names = [d.name for d in self.departments] if self.departments else []
        current_department_name = self.current_department.name if self.current_department else ""
        return department_names, current_department_name

    def load_all_divisions(self) -> None:
        divisions = self._employee_service.load_all_divisions()
        self.divisions = divisions

    def change_current_division(self, division_name: str) -> None:
        division = next((d for d in self.divisions if d.name == division_name), None)
        self.current_division = division

    def change_current_department(self, department_name: str) -> None:
        department = next((d for d in self.departments if d.name == department_name), None)
        self.current_department = department
