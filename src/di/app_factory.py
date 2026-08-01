from __future__ import annotations

from typing import TYPE_CHECKING

from src.presentation.presenters import EmployeesPresenter
from src.data.repositories import EmployeesRepository
from src.presentation.gui.views import EmployeesScreen, MainMenuScreen
from src.presentation.presenters import MainMenuPresenter

if TYPE_CHECKING:
    from src.coordinators.app_coordinator import AppCoordinator
    from src.data.db_manager import DatabaseManager


class AppFactory:
    def __init__(self, *, db_connect: DatabaseManager) -> None:
        self._employees_repo = EmployeesRepository(db_connect)

    def create_main_menu_screen(self, coordinator: AppCoordinator) -> MainMenuScreen:
        main_menu_screen = MainMenuScreen()
        main_menu_presenter = MainMenuPresenter(main_menu_screen, self._employees_repo)

        main_menu_presenter.close_app_signal.connect(coordinator.close_app)
        main_menu_presenter.open_employees_view_signal.connect(coordinator.show_employees_screen)
        main_menu_presenter.open_reports_view_signal.connect(coordinator.show_reports_view)
        main_menu_presenter.open_protocols_view_signal.connect(coordinator.show_protocols_view)

        return main_menu_screen

    def create_employees_view_screen(
        self, coordinator: AppCoordinator, company_id: int
    ) -> EmployeesScreen:
        employees_screen = EmployeesScreen()
        employees_presenter = EmployeesPresenter(company_id, employees_screen, self._employees_repo)
        employees_presenter.open_main_menu_screen_signal.connect(coordinator.show_main_menu_screen)
        return employees_screen
