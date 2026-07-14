from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from src.shared.constants import QtStyleResources

from ..generated import ResourceLoader, Ui_MainMenuWidget
from .base_widget import BaseWidget


class MainMenuWidget(BaseWidget, Ui_MainMenuWidget):
    open_reports_window_signal = Signal()
    open_protocols_window_signal = Signal()
    close_app_signal = Signal()

    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        self.init_content_view()
        self.setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_MENU_STYLE).load_style())

    def setup_connections(self) -> None:
        self.pushButton_exit.clicked.connect(self.close_app_signal.emit)
        self.pushButton_create_sheets.clicked.connect(self.open_reports_window_signal.emit)
        self.pushButton_create_protocols.clicked.connect(self.open_protocols_window_signal.emit)
