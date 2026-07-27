from __future__ import annotations

from typing import TYPE_CHECKING

from src.coordinators.coordinator import Coordinator
from src.shared.constants import AppWindowViews as AppViews

if TYPE_CHECKING:
    from views.base_view import BaseView

    from di import AppFactory
    from shared.constants import PageStructure
    from src.presentation.gui import MainWindow


class AppCoordinator(Coordinator):
    def __init__(self, *, app_factory: AppFactory, main_window: MainWindow) -> None:
        super().__init__(app_factory)
        self._app_factory = app_factory
        self._window = main_window
        self._stacked_widgets = main_window.stackedWidget_windows
        self._widgets: dict[PageStructure, BaseView] = {}

    def start(self) -> None:
        self._window.show()
        self.show_main_menu_view()

    def show_main_menu_view(self) -> None:
        if AppViews.MAIN_MENU not in self._widgets:
            main_menu_view = self._app_factory.create_main_menu_screen(self)
            self._widgets[AppViews.MAIN_MENU] = main_menu_view
            self._stacked_widgets.addWidget(main_menu_view)
        self._stacked_widgets.setCurrentWidget(self._widgets[AppViews.MAIN_MENU])

    def close_app(self) -> None:
        self._window.close()

    def show_employees_view(self, company_id: int) -> None:
        # if AppViews
        print(f"в координатор для работников пришла компания: {company_id}")

    def show_reports_view(self, company_id: int) -> None:
        print(f"в координатор для отчетов пришла компания: {company_id}")

    def show_protocols_view(self, company_id: int) -> None:
        print(f"в координатор для протоколов пришла компания: {company_id}")
