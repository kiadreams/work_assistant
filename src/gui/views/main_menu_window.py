from PySide6.QtCore import Signal

from src.core.constants import QtStyleResources
from src.gui.generated import Ui_MainMenuWidget
from src.gui.utils import ResourceLoader
from src.gui.views.base_views import BaseView


class MainMenuWindow(BaseView, Ui_MainMenuWidget):
    open_reports_window_signal = Signal()
    open_protocols_window_signal = Signal()
    close_app_signal = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.init_content_view()
        self.setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_MENU_STYLE).load_style())

    def setup_connections(self) -> None:
        self.pushButton_exit.clicked.connect(self.close_app_signal.emit)
        self.pushButton_create_sheets.clicked.connect(self.open_reports_window_signal.emit)
        self.pushButton_create_protocols.clicked.connect(self.open_protocols_window_signal.emit)
