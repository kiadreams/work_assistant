from PySide6 import QtWidgets

from . import resources_rc
from .resource_loader import QtStyleResources, ResourceLoader
from .qtforms.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app_version):
        super().__init__()
        self.app_version = app_version
        self.setupUi(self)
        self.setStyleSheet(ResourceLoader(QtStyleResources.STANDARD_STYLE).load_style())
        self.setFixedSize(800, 600)
        self.__init_text_ui()
        self.__setup_connections()

    def __init_text_ui(self):
        self.lbl_app_version.setText(f'Версия приложения: {self.app_version}')

    def __setup_connections(self):
        self.psb_exit.clicked.connect(self.close)
        self.psb_create_sheets.clicked.connect(self.create_sheets)
        self.psb_create_protocols.clicked.connect(self.create_protocols)

    def create_sheets(self):
        self.pte_logs.appendPlainText('нажали кнопку создания рабочих ведомостей'.upper())

    def create_protocols(self):
        self.pte_logs.appendPlainText('пока данный функционал в разработке'.upper())
