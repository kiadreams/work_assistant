from src.gui.constants import MainWindows as Windows
from src.gui.coordinators.reports_coordinator import ReportsCoordinator
from src.gui.interfaces.coordinators import SessionCoordinatorProtocol
from src.gui.views import MainMenuWindow, MainWindow
from src.services.interfaces.services import EmployeeServiceProtocol


class AppCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service
        self.main_window = MainWindow()
        self.main_menu_window = MainMenuWindow()
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
        if self.session_coordinator:
            self.session_coordinator = None

    def open_reports_window(self) -> None:
        self.main_menu_window.plainTextEdit_logs.appendPlainText(
            "Нажали кнопку открытия окна создания отчётов"
        )
        self.session_coordinator = ReportsCoordinator(self.employee_service)
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
