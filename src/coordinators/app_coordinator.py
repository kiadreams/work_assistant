from __future__ import annotations

from typing import TYPE_CHECKING

from src.shared.constants import AppScreen

if TYPE_CHECKING:
    from src.di.app_factory import AppFactory
    from src.presentation.gui import MainWindow
    from src.presentation.gui.views import BaseView
    from src.shared.constants import PageStructure


class AppCoordinator:
    def __init__(self, *, app_factory: AppFactory, main_window: MainWindow) -> None:
        self._app_factory = app_factory
        self._window = main_window
        self._stacked_widgets = main_window.stackedWidget_windows
        self._widgets: dict[PageStructure, BaseView] = {}

    def start(self) -> None:
        self._window.show()
        self.show_main_menu_screen()

    def close_app(self) -> None:
        self._window.close()

    def show_main_menu_screen(self) -> None:
        if AppScreen.MAIN_MENU not in self._widgets:
            main_menu_screen = self._app_factory.create_main_menu_screen(self)
            self._widgets[AppScreen.MAIN_MENU] = main_menu_screen
            self._stacked_widgets.addWidget(main_menu_screen)
        self._stacked_widgets.setCurrentWidget(self._widgets[AppScreen.MAIN_MENU])

    def show_employees_screen(self, company_id: int) -> None:
        if AppScreen.EMPLOYEES not in self._widgets:
            employees_screen = self._app_factory.create_employees_view_screen(self, company_id)
            self._widgets[AppScreen.EMPLOYEES] = employees_screen
            self._stacked_widgets.addWidget(employees_screen)
        self._stacked_widgets.setCurrentWidget(self._widgets[AppScreen.EMPLOYEES])

    def show_reports_view(self, company_id: int) -> None:
        print(f"в координатор для отчетов пришла компания: {company_id}")

    def show_protocols_view(self, company_id: int) -> None:
        print(f"в координатор для протоколов пришла компания: {company_id}")
