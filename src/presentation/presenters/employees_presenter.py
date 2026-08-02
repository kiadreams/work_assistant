from __future__ import annotations

from typing import TYPE_CHECKING, cast

from PySide6.QtCore import QObject, Signal

from ..gui.views import EmployeesScreen
from ..view_dtos import DepartmentViewDto, DivisionViewDto, EmployeeViewDto

if TYPE_CHECKING:
    from employees_repository import EmployeesRepository


class EmployeesPresenter(QObject):
    open_main_menu_screen_signal = Signal()

    def __init__(
        self,
        company_id: int,
        employees_screen: EmployeesScreen,
        employees_repo: EmployeesRepository,
    ) -> None:
        super().__init__(employees_screen)
        self.company_id = company_id
        self._staff_repo = employees_repo
        self.start()

    @property
    def view(self) -> EmployeesScreen:
        return cast(EmployeesScreen, self.parent())

    def start(self) -> None:
        self._connect_signals()
        self.load_view_data()

    def _connect_signals(self) -> None:
        self.view.to_main_menu_signal.connect(self._open_main_menu_screen)
        self.view.employee_addition_signal.connect(self._add_new_employee)
        self.view.employee_removal_signal.connect(self._delete_employee)
        self.view.division_list_changed_signal.connect(self._show_division_departments)
        self.view.show_division_employees_signal.connect(self._show_division_employees)
        self.view.show_department_employees_signal.connect(self._show_department_employees)
        self.view.clear_employee_table_signal.connect(self._clear_employees_table)

    def _open_main_menu_screen(self) -> None:
        self.open_main_menu_screen_signal.emit()

    def load_view_data(self) -> None:
        divisions_dmn = self._staff_repo.get_company_divisions(self.company_id)
        divisions_dto = [
            DivisionViewDto.from_domain(division_dmn) for division_dmn in divisions_dmn
        ]
        self.view.set_company_divisions(divisions_dto)

    def _add_new_employee(self) -> None:
        pass

    def _delete_employee(self) -> None:
        pass

    def _show_division_departments(self, division: DivisionViewDto) -> None:
        departments_dmn = self._staff_repo.get_division_departments(division.id)
        departments_dto = [
            DepartmentViewDto.from_domain(department_dmn) for department_dmn in departments_dmn
        ]
        self.view.set_division_departments(departments_dto)

    def _show_division_employees(self, division: DivisionViewDto) -> None:
        employees_dmn = self._staff_repo.get_division_employees(division.id)
        employees_dto = [
            EmployeeViewDto.from_domain(employee_dmn) for employee_dmn in employees_dmn
        ]
        self.view.set_employees_data(employees_dto)

    def _show_department_employees(self, department: DepartmentViewDto) -> None:
        employees_dmn = self._staff_repo.get_department_employees(department.id)
        employees_dto = [
            EmployeeViewDto.from_domain(employee_dmn) for employee_dmn in employees_dmn
        ]
        self.view.set_employees_data(employees_dto)

    def _clear_employees_table(self) -> None:
        self.view.set_employees_data([])
