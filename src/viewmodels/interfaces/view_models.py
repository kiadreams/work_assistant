from typing import Protocol

from PySide6.QtCore import SignalInstance

from src.core.models.domain_models import DivisionDomain, DepartmentDomain


class BaseViewModelProtocol(Protocol):
    def init_model_data(self) -> None: ...


class DivisionViewModelProtocol(BaseViewModelProtocol, Protocol):
    division_data_changed_signal: SignalInstance
    department_data_changed_signal: SignalInstance

    @property
    def divisions(self) -> list[DivisionDomain]: ...

    @divisions.setter
    def divisions(self, value: list[DivisionDomain]) -> None: ...

    @property
    def current_division(self) -> DivisionDomain | None: ...

    @current_division.setter
    def current_division(self, division: DivisionDomain | None) -> None: ...

    @property
    def departments(self) -> list[DepartmentDomain]: ...

    @departments.setter
    def departments(self, value: list[DepartmentDomain]) -> None: ...

    @property
    def current_department(self) -> DepartmentDomain | None: ...

    @current_department.setter
    def current_department(self, department: DepartmentDomain | None) -> None: ...

    def load_all_divisions(self) -> None: ...

    @property
    def can_delete_current_division(self) -> bool: ...

    @property
    def can_edit_current_division(self) -> bool: ...

    @property
    def can_show_all_divisions(self) -> bool: ...

    @property
    def can_delete_current_department(self) -> bool: ...

    @property
    def can_edit_current_department(self) -> bool: ...

    @property
    def can_show_departments_of_division(self) -> bool: ...

    def change_current_division(self, division_name: str) -> None: ...

    def change_current_department(self, department_name: str) -> None: ...
