from __future__ import annotations

from typing import TYPE_CHECKING

from src.core.constants import MainWindows as Windows
from src.gui.coordinators.reports_coordinator import ReportsCoordinator
from src.gui.views import MainMenuWindow, MainWindow

if TYPE_CHECKING:
    from dependency_injector.providers import Factory

    from core.interfaces.coordinators import SessionCoordinatorProtocol
    from core.interfaces.services import EmployeeServiceProtocol
    from di.sessions_container import SessionsContainer


class AppCoordinator:
    def __init__(
        self,
        main_window: MainWindow,
        main_menu_window: MainMenuWindow,
        sessions_factory: Factory[SessionsContainer],
    ) -> None:
        self.main_window = main_window
        self.main_menu_window = main_menu_window
        self.sessions_factory = sessions_factory
        self.session_coordinator: SessionCoordinatorProtocol | None = None

    def start_app(self) -> None:
        self.main_window.add_window(Windows.MAIN_MENU, self.main_menu_window)
        self.main_window.show()
        self._connect_signals()

    def _connect_signals(self) -> None:
        self.main_menu_window.open_reports_window_signal.connect(self.open_reports_window)
        self.main_menu_window.open_protocols_window_signal.connect(self.open_protocols_window)
        self.main_menu_window.close_app_signal.connect(self.main_window.close)

    def open_main_menu_window(self) -> None:
        self.main_window.change_window(Windows.MAIN_MENU)
        self._close_current_session()

    def open_reports_window(self) -> None:
        self.main_menu_window.plainTextEdit_logs.appendPlainText(
            "Нажали кнопку открытия окна создания отчётов"
        )
        self.session_coordinator = self.sessions_factory().reports_coordinator()
        self.session_coordinator.start_session()
        self.session_coordinator.session_window.back_main_menu_signal.connect(
            self.open_main_menu_window
        )
        self.main_window.add_window(Windows.REPORTS_WINDOW, self.session_coordinator.session_window)
        self.main_window.change_window(Windows.REPORTS_WINDOW)

    def open_protocols_window(self) -> None:
        self.main_menu_window.plainTextEdit_logs.appendPlainText(
            "Нажали кнопку открытия окна создания протоколов"
        )
        self.main_window.change_window(Windows.PROTOCOLS_WINDOW)

    def _close_current_session(self) -> None:
        if self.session_coordinator:
            # 1. Сначала просим сам координатор сессии очистить его внутренние ресурсы
            if hasattr(self.session_coordinator, "teardown"):
                self.session_coordinator.teardown()
            # 2. Просим Qt удалить объект виджета из памяти
            if self.session_coordinator.session_window:
                self.session_coordinator.session_window.deleteLater()
            # 3. Обнуляем ссылку на координатор
            self.session_coordinator = None
