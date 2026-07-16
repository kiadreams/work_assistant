from __future__ import annotations

from typing import TYPE_CHECKING

from src.presentation.presenters.base_presenters.base_presenter import BasePresenter
from src.shared.constants import MainWindows as Windows
from src.shared.exceptions.base_exceptions import ViewFormError

if TYPE_CHECKING:
    from presentation.gui.views import MainMenuWidget
    from src.coordinators import MainWindowCoordinator


class MainMenuPresenter(BasePresenter):
    def __init__(
        self,
        coordinator: MainWindowCoordinator,
        main_menu_widget: MainMenuWidget,
        widget_index: int,
    ) -> None:
        super().__init__(coordinator, widget_index)
        self.main_menu = main_menu_widget

    def start(self) -> None:
        self.__connect_signals()

    def __connect_signals(self) -> None:
        self.main_menu.open_reports_window_signal.connect(self.__open_reports_window)
        self.main_menu.open_protocols_window_signal.connect(self.__open_protocols_window)
        self.main_menu.close_app_signal.connect(self.main_window.close)

    def __disconnect_signals(self) -> None:
        self.main_menu.open_reports_window_signal.disconnect(self.__open_reports_window)
        self.main_menu.open_protocols_window_signal.disconnect(self.__open_protocols_window)
        self.main_menu.close_app_signal.disconnect(self.main_window.close)

    def open_main_menu_window(self) -> None:
        self.main_window.show_widget(Windows.MAIN_MENU)
        self._close_current_session()

    def __open_reports_window(self) -> None:
        self.main_menu_window.plainTextEdit_logs.appendPlainText(
            "Нажали кнопку открытия окна создания отчётов"
        )
        session = self.session_reports_factory()
        self.session_coordinator = session.reports_coordinator()
        if not self.session_coordinator:
            raise ViewFormError
        self.session_coordinator.session_window.back_main_menu_signal.connect(
            self.open_main_menu_window
        )
        self.session_coordinator.start()
        self.main_window.add_widget(Windows.REPORTS_WINDOW, self.session_coordinator.session_window)
        self.main_window.show_widget(Windows.REPORTS_WINDOW)

    def __open_protocols_window(self) -> None:
        self.main_menu_window.plainTextEdit_logs.appendPlainText(
            "Нажали кнопку открытия окна создания протоколов"
        )
        self.main_window.show_widget(Windows.PROTOCOLS_WINDOW)

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

    def teardown(self) -> None:
        if self.session_coordinator:
            self.session_coordinator.teardown()
        self.__disconnect_signals()
        self.main_menu_window.deleteLater()
        self.main_window.deleteLater()
        print("Закрываем координатор")

