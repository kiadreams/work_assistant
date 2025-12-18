from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from .. import resources_rc
from ..resource_loader import QtStyleResources, ResourceLoader
from ..views_structure import MainWindowPages
from ..forms.ui_main_menu_widget import Ui_MainMenuWidget


class MainMenu(QtWidgets.QWidget, Ui_MainMenuWidget):

    change_page_signal = Signal(int)
    close_app_signal = Signal()

    def __init__(self, app_version: str) -> None:
        super().__init__()
        self.app_version = app_version
        self.setupUi(self)
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_MENU_STYLE).load_style())
        self.__init_content_app()
        self.__setup_connections()

    def __init_content_app(self) -> None:
        self.lbl_app_version.setText(f'Версия приложения: {self.app_version}')

    def __setup_connections(self) -> None:
        self.psb_exit.clicked.connect(self.close_app_signal.emit)
        self.psb_create_sheets.clicked.connect(self.create_sheets)
        self.psb_create_protocols.clicked.connect(self.create_protocols)

    def create_sheets(self) -> None:
        self.pte_logs.appendPlainText('нажали кнопку создания рабочих ведомостей'.upper())
        self.change_page_signal.emit(MainWindowPages.REPORT_CREATION)

    def create_protocols(self) -> None:
        self.pte_logs.appendPlainText('пока данный функционал в разработке'.upper())
