from __future__ import annotations

from typing import TYPE_CHECKING, cast

from PySide6.QtCore import QObject, Signal, SignalInstance

from ..gui.views import EmployeesScreen

if TYPE_CHECKING:
    from employees_repository import EmployeesRepository


class EmployeesPresenter(QObject):
    to_main_menu_screen_signal = Signal()

    def __init__(
        self,
        company_id: int,
        employees_screen: EmployeesScreen,
        employees_repo: EmployeesRepository,
    ) -> None:
        super().__init__(employees_screen)
        self.company_id = company_id
        self._company_repo = employees_repo
        self.start()

    @property
    def view(self) -> EmployeesScreen:
        return cast(EmployeesScreen, self.parent())

    def start(self) -> None:
        self._connect_signals()
        self.load_view_data()

    def _connect_signals(self) -> None:
        pass

    def teardown(self) -> None:
        pass

    def load_view_data(self):
        pass
