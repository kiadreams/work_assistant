from __future__ import annotations

from typing import TYPE_CHECKING, cast

from PySide6.QtCore import QObject, Signal, SignalInstance

from ..gui.views import MainMenuScreen

if TYPE_CHECKING:
    from employees_repository import EmployeesRepository


class MainMenuPresenter(QObject):
    open_employees_view_signal = Signal(int)
    open_reports_view_signal = Signal(int)
    open_protocols_view_signal = Signal(int)
    close_app_signal = Signal()

    def __init__(
        self, main_menu_screen: MainMenuScreen, employees_repo: EmployeesRepository
    ) -> None:
        super().__init__(main_menu_screen)
        self._company_repo = employees_repo
        self.start()

    @property
    def view(self) -> MainMenuScreen:
        return cast(MainMenuScreen, self.parent())

    def start(self) -> None:
        self._connect_signals()
        self.load_view_data()

    def _connect_signals(self) -> None:
        self.view.close_app_click_signal.connect(self.close_app_signal.emit)
        self.view.employees_view_click_signal.connect(self._open_employees_view)
        self.view.reports_view_click_signal.connect(self._open_reports_view)
        self.view.protocols_view_click_signal.connect(self._open_protocols_view)

    def load_view_data(self):
        companies = self._company_repo.get_all_companies()
        companies_data = {
            company.full_name if company.full_name else company.name: company.id
            for company in companies
        }
        print(companies_data)
        self.view.display_companies(companies_data)

    def _open_employees_view(self, company_id: int) -> None:
        self._emit_open_view_signal(self.open_employees_view_signal, company_id)

    def _open_reports_view(self, company_id: int) -> None:
        self._emit_open_view_signal(self.open_reports_view_signal, company_id)

    def _open_protocols_view(self, company_id: int) -> None:
        self._emit_open_view_signal(self.open_protocols_view_signal, company_id)

    def _emit_open_view_signal(self, signal: SignalInstance, company_id: int) -> None:
        if self._company_repo.is_company_id_exists(company_id):
            signal.emit(company_id)
