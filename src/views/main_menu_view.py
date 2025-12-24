from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from ..utils.qt_recource_loader import ResourceLoader
from ..constants import MainWindowPages, QtStyleResources
from .generated.ui.ui_main_menu_widget import Ui_MainMenuWidget


class MainMenuView(QtWidgets.QWidget, Ui_MainMenuWidget):

    change_page_signal = Signal(int)
    close_app_signal = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_MENU_STYLE).load_style())

    def __setup_connections(self) -> None:
        self.pushButton_exit.clicked.connect(self.close_app_signal.emit)
        self.pushButton_create_sheets.clicked.connect(self.create_sheets)
        self.pushButton_create_protocols.clicked.connect(self.create_protocols)

    def create_sheets(self) -> None:
        self.plainTextEdit_logs.appendPlainText("нажали кнопку создания рабочих ведомостей".upper())
        self.change_page_signal.emit(MainWindowPages.REPORT_CREATION)

    def create_protocols(self) -> None:
        self.plainTextEdit_logs.appendPlainText("пока данный функционал в разработке".upper())
