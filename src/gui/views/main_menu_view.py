from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_MainMenuWidget
from src.utils.qt_recource_loader import ResourceLoader


class MainMenuView(QtWidgets.QWidget, Ui_MainMenuWidget):
    open_reports_window_signal = Signal()
    open_protocols_window_signal = Signal()
    close_app_signal = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.init_content_view()
        self.__setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_MENU_STYLE).load_style())

    def __setup_connections(self) -> None:
        self.pushButton_exit.clicked.connect(self.close_app_signal.emit)
        self.pushButton_create_sheets.clicked.connect(self.open_reports_window_signal.emit)
        self.pushButton_create_protocols.clicked.connect(self.open_protocols_window_signal.emit)

    # def create_sheets(self) -> None:
    #     self.plainTextEdit_logs.appendPlainText("нажали кнопку создания рабочих ведомостей".upper())
    #     self.open_reports_window_signal.emit(MainWindowPages.REPORTS_WINDOW)
    #
    # def create_protocols(self) -> None:
    #     self.plainTextEdit_logs.appendPlainText("пока данный функционал в разработке".upper())
    #     self.open_protocols_window_signal.emit(MainWindowPages.REPORTS_WINDOW)
