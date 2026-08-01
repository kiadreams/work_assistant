from __future__ import annotations

from typing import TYPE_CHECKING, cast

from PySide6.QtCore import QObject, Signal

from ..gui.views import EmployeesScreen

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
        self.view.to_main_menu_click_signal.connect(self._open_main_menu_screen)
        self.view.add_employee_signal.connect(self._add_new_employee)
        self.view.delete_employee_signal.connect(self._delete_employee)

    def _open_main_menu_screen(self) -> None:
        self.open_main_menu_screen_signal.emit()

    def load_view_data(self):
        divisions = self._staff_repo.get_company_divisions(self.company_id)


    def _add_new_employee(self) -> None:
        pass

    def _delete_employee(self) -> None:
        pass
