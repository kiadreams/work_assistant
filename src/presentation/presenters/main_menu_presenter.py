from __future__ import annotations

from typing import TYPE_CHECKING, cast

from PySide6.QtCore import QObject, Signal

from src.presentation.view_dtos.staff_view_dtos import CompanyViewDto

from ..gui.views import MainMenuScreen

if TYPE_CHECKING:
    from employees_repository import EmployeesRepository


class MainMenuPresenter(QObject):
    open_employees_screen_signal = Signal(int)
    open_reports_screen_signal = Signal(int)
    open_protocols_screen_signal = Signal(int)
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
        self.view.close_app_signal.connect(self.close_app_signal.emit)
        self.view.to_employees_screen_signal.connect(self._open_employees_screen)
        self.view.to_reports_screen_signal.connect(self._open_reports_screen)
        self.view.to_protocols_screen_signal.connect(self._open_protocols_screen)

    def load_view_data(self):
        companies_dmn = self._company_repo.get_all_companies()
        companies_dto = [CompanyViewDto.from_domain(company_dmn) for company_dmn in companies_dmn]
        self.view.set_companies_data(companies_dto)

    def _open_employees_screen(self, company_dto: CompanyViewDto) -> None:
        self.open_employees_screen_signal.emit(company_dto.id)

    def _open_reports_screen(self, company_dto: CompanyViewDto) -> None:
        self.open_reports_screen_signal.emit(company_dto.id)

    def _open_protocols_screen(self, company_dto: CompanyViewDto) -> None:
        self.open_protocols_screen_signal.emit(company_dto.id)
