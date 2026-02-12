from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Signal

from src.core.exceptions.db_exceptions import (
    DivisionNotFoundError,
    DepartmentNotFoundError,
    DivisionTypeError,
    DepartmentTypeError,
    EntityAttributeTypeError,
)
from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain
from src.gui.viewmodels.base_view_model import BaseViewModel

if TYPE_CHECKING:
    from src.core.services import EmployeeService


class DivisionViewModel(BaseViewModel):
    division_data_changed_signal = Signal()
    department_data_changed_signal = Signal()

    def __init__(
        self,
        employee_service: EmployeeService,
    ) -> None:
        super().__init__()
        self._employee_service = employee_service
        self._divisions: list[DivisionDomain] = []
        self._current_division: DivisionDomain | None = None
        self._departments: list[DepartmentDomain] = []
        self._current_department: DepartmentDomain | None = None
        self._new_division: DivisionDomain | None = None
        self._new_department: DepartmentDomain | None = None

    def init_model_data(self) -> None:
        self.load_all_divisions()

    @property
    def divisions(self) -> list[DivisionDomain]:
        return self._divisions

    @divisions.setter
    def divisions(self, value: list[DivisionDomain]) -> None:
        self._divisions = value
        self.current_division = value[0] if value else None

    @property
    def current_division(self) -> DivisionDomain | None:
        return self._current_division

    @current_division.setter
    def current_division(self, division: DivisionDomain | None) -> None:
        self._current_division = division
        self.departments = division.departments if division else []
        self.division_data_changed_signal.emit()

    @property
    def departments(self) -> list[DepartmentDomain]:
        return self._departments

    @departments.setter
    def departments(self, value: list[DepartmentDomain]) -> None:
        self._departments = value
        self.current_department = value[0] if value else None

    @property
    def current_department(self) -> DepartmentDomain | None:
        return self._current_department

    @current_department.setter
    def current_department(self, department: DepartmentDomain | None) -> None:
        self._current_department = department
        self.department_data_changed_signal.emit()

    @property
    def can_delete_current_division(self) -> bool:
        if self.current_division and not self.departments:
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
    def division_name_data(self) -> tuple[list[str], str]:
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

    def add_new_division(self, division: DivisionDomain) -> None:
        new_division = self._employee_service.add_new_division(division)
        self.divisions.append(new_division)
        self.current_division = new_division
        print(new_division)

    def add_new_department(self, department: DepartmentDomain) -> None:
        new_department = self._employee_service.add_new_department(department)
        self.departments.append(new_department)
        self.current_department = new_department

    def delete_current_division(self) -> None:
        if not self.current_division:
            return
        division_id = self.current_division.id
        try:
            self._employee_service.delete_division_by_id(division_id)
        except EntityAttributeTypeError as e:
            self.error_generation_signal.emit(e)
        else:
            self.divisions.remove(self.current_division)
            self.current_division = self.divisions[0] if self.divisions else None

    def delete_current_department(self) -> None:
        if not self.current_department:
            return
        department_id = self.current_department.id
        try:
            self._employee_service.delete_department_by_id(department_id)
        except EntityAttributeTypeError as e:
            self.error_generation_signal.emit(e)
        self.departments.remove(self.current_department)
        self.current_department = self.departments[0] if self.departments else None

    def edit_current_division(self, division: DivisionDomain) -> None:
        if self.current_division:
            print(f"Нажали править отдел с текущим именем: {self.current_division.name}")

    def edit_current_department(self, department: DepartmentDomain) -> None:
        if self.current_division:
            print(f"Нажали править отдел с текущим именем: {self.current_division.name}")
