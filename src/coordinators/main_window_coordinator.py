from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from coordinators.base_coordinator import BaseCoordinator
from src.presentation.gui import MainMenuWidget, MainWindow
from src.presentation.presenters import MainMenuPresenter

if TYPE_CHECKING:
    from di import AppFactory
    from src.presentation.presenters import BasePresenter


class WindowWidgets(StrEnum):
    MAIN_MENU = "main_menu_widget"
    REPORTS = "reports_widget"
    PROTOCOLS = "protocols_widget"


class MainWindowCoordinator(BaseCoordinator):
    def __init__(self, app_factory: AppFactory, main_window: MainWindow) -> None:
        super().__init__(app_factory)
        self.__app_factory = app_factory
        self.window = main_window
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
