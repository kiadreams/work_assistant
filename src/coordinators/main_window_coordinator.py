from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from src.data import DatabaseManager
from src.data.repositories.app_repository import AppRepository
from src.presentation.gui import MainMenuWidget, MainWindow
from src.presentation.presenters import MainMenuPresenter

if TYPE_CHECKING:
    from src.presentation.presenters import BasePresenter


class WindowWidgets(StrEnum):
    MAIN_MENU = "main_menu_widget"
    REPORTS = "reports_widget"
    PROTOCOLS = "protocols_widget"


class MainWindowCoordinator:
    def __init__(
        self, main_window: MainWindow, db_manager: DatabaseManager, app_repo: AppRepository
    ) -> None:
        self.window = MainWindow()
        self.db_manager = DatabaseManager()
        self.app_repository = AppRepository(self.db_manager)
        self.widgets: dict[str, BasePresenter] = {}

    def start(self) -> None:
        self.show_main_menu()
        self.window.show()

    def show_main_menu(self) -> None:
        if WindowWidgets.MAIN_MENU not in self.widgets:
            self.__create_main_menu()
        self.window.show_widget(self.widgets[WindowWidgets.MAIN_MENU].widget_index)

    def __create_main_menu(self) -> None:
        main_menu_widget = MainMenuWidget(self.window)
        widget_index = self.window.add_widget(main_menu_widget)
        main_menu_presenter = MainMenuPresenter(self, main_menu_widget, widget_index)
        self.widgets[WindowWidgets.MAIN_MENU] = main_menu_presenter

    # def __create_reports(self) -> None:
    #
    #     reports_presenter = ReportsPresenter(self, ReportsWidget(self.window))
