from src.core.interfaces.factories import AppFactoryProtocol

from ...core.interfaces.ui import (
    MainMenuViewProtocol,
    MainWindowViewProtocol,
    ReportsWindowViewProtocol,
)
from ..constants import MainWindowPages


class AppCoordinator:
    def __init__(self, window_factory: AppFactoryProtocol) -> None:
        super().__init__()
        self.factory = window_factory
        self.main_window: MainWindowViewProtocol | None = None
        self.main_menu: MainMenuViewProtocol | None = None
        self.reports_window: ReportsWindowViewProtocol | None = None

    def start_app(self) -> None:
        self.main_window = self.factory.main_window
        self.main_menu = self.factory.main_menu
        self.reports_window = self.factory.reports_window
        self.main_window.insert_into_stacked_windows(
            MainWindowPages.MAIN_MENU,
            self.main_menu,
        )
        self.main_window.insert_into_stacked_windows(
            MainWindowPages.REPORTS_WINDOW,
            self.reports_window,
        )
        self.open_main_menu_window()
        self.main_window.show()
        self._connect_signals()

    def _connect_signals(self) -> None:
        if self.main_menu and self.main_window:
            self.main_menu.open_reports_window_signal.connect(self.open_reports_window)
            self.main_menu.open_protocols_window_signal.connect(self.open_protocols_window)
            self.main_menu.close_app_signal.connect(self.main_window.close)
        if self.reports_window:
            self.reports_window.back_main_menu_signal.connect(self.open_main_menu_window)

    def open_main_menu_window(self) -> None:
        self.__open_window(MainWindowPages.MAIN_MENU)

    def open_reports_window(self) -> None:
        with self.factory.start_reports_session() as reports_coordinator:
            reports_coordinator.start_report_session()
            self.__open_window(MainWindowPages.REPORTS_WINDOW)
            print("ресурсы отчетов уничтожены")

    def open_protocols_window(self) -> None:
        self.__open_window(MainWindowPages.PROTOCOLS_WINDOW)
        print("Нажали кнопку создания протоколов!!!")

    def __open_window(self, index: MainWindowPages) -> None:
        if self.main_window:
            self.main_window.change_page(index)
