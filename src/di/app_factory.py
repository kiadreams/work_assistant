from __future__ import annotations

from typing import TYPE_CHECKING

from src.data.repositories.reports_repositories.company_repository import CompanyRepository
from src.di.factory import Factory
from src.presentation.gui import MainMenuView
from src.presentation.presenters import MainMenuPresenter

if TYPE_CHECKING:
    from db_manager import DatabaseManager

    from coordinators import AppCoordinator

class AppFactory(Factory):
    def __init__(self, *, db_connect: DatabaseManager) -> None:
        super().__init__(db_connect)

    def create_main_menu_screen(self, coordinator: AppCoordinator) -> MainMenuView:
        company_repo = CompanyRepository(self.db_connect)
        main_menu_view = MainMenuView()
        main_menu_presenter = MainMenuPresenter(main_menu_view, company_repo)
        main_menu_presenter.close_app_signal.connect(coordinator.close_app)
        main_menu_presenter.open_employees_view_signal.connect(coordinator.show_employees_view)
        main_menu_presenter.open_reports_view_signal.connect(coordinator.show_reports_view)
        main_menu_presenter.open_protocols_view_signal.connect(coordinator.show_protocols_view)
        return main_menu_view
