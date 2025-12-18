from PySide6 import QtWidgets

from .main_menu import MainMenu
from .report_generator import ReportGenerator
from .. import resources_rc
from ..resource_loader import QtStyleResources, ResourceLoader
from ..forms.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app_version: str) -> None:
        super().__init__()
        self.app_version = app_version
        self.setupUi(self)
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_WINDOW_STYLE).load_style())
        self.main_menu = MainMenu(self.app_version)
        self.report_generator = ReportGenerator()
        self.__set_main_windows_widgets()
        self.__connect_signals()

    def __set_main_windows_widgets(self) -> None:
        main_menu_layout = QtWidgets.QVBoxLayout()
        main_menu_layout.addWidget(self.main_menu)
        self.main_menu.setLayout(main_menu_layout)

        report_generator_layout = QtWidgets.QVBoxLayout()
        report_generator_layout.addWidget(self.report_generator)
        self.report_generator.setLayout(report_generator_layout)

        self.stcWdgt_windows.insertWidget(0, self.main_menu)
        self.stcWdgt_windows.insertWidget(1, self.report_generator)

        self.stcWdgt_windows.setCurrentIndex(0)

    def __connect_signals(self) -> None:
        self.main_menu.close_app_signal.connect(self.close)
        self.main_menu.change_page_signal.connect(self.change_page)
        self.report_generator.change_page_signal.connect(self.change_page)

    def change_page(self, index: int) -> None:
        self.stcWdgt_windows.setCurrentIndex(index)




    # def __setup_connections(self):
    #     self.psb_exit.clicked.connect(self.close)
    #     self.psb_create_sheets.clicked.connect(self.create_sheets)
    #     self.psb_create_protocols.clicked.connect(self.create_protocols)
    #
    # def create_sheets(self):
    #     self.pte_logs.appendPlainText('нажали кнопку создания рабочих ведомостей'.upper())
    #     self.stcWdgt_windows.setCurrentIndex(1)
    #
    # def create_protocols(self):
    #     self.pte_logs.appendPlainText('пока данный функционал в разработке'.upper())
