from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from src.shared.constants import QtStyleResources

from ..generated import ResourceLoader, Ui_MainMenuWidget
from .base_view import BaseView


class MainMenuView(BaseView, Ui_MainMenuWidget):
    employees_view_click_signal = Signal(int)
    reports_view_click_signal = Signal(int)
    protocols_view_click_signal = Signal(int)
    close_app_click_signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.init_content_view()
        self.setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_MENU_STYLE).load_style())

    def setup_connections(self) -> None:
        self.pushButton_exit.clicked.connect(self.close_app_click_signal.emit)
        self.pushButton_edit_employees.clicked.connect(self._open_employees_view)
        self.pushButton_create_sheets.clicked.connect(self._open_reports_view)
        self.pushButton_create_protocols.clicked.connect(self._open_protocols_view)

    def display_companies(self, companies: dict[str, int]) -> None:
        for name, company_id in companies.items():
            self.comboBox_companies.addItem(name, company_id)

    def _open_employees_view(self) -> None:
        self.employees_view_click_signal.emit(self._get_selected_company_id())

    def _open_reports_view(self) -> None:
        self.reports_view_click_signal.emit(self._get_selected_company_id())

    def _open_protocols_view(self) -> None:
        self.protocols_view_click_signal.emit(self._get_selected_company_id())

    def _get_selected_company_id(self) -> int:
        if self.comboBox_companies.currentIndex() != -1:
            return self.comboBox_companies.currentData()
        return -1
