from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from .. import resources_rc
from ..resource_loader import QtStyleResources, ResourceLoader
from ..views_structure import MainWindowPages
from ..forms.ui_report_generation_widget import Ui_ReportGenerationWidget


class ReportGenerator(QtWidgets.QWidget, Ui_ReportGenerationWidget):

    change_page_signal = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        # self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_MENU_STYLE).load_style())
        # self.__init_content_app()
        self.__setup_connections()

    # def __init_content_app(self):
    #     self.lbl_app_version.setText(f'Версия приложения: {self.app_version}')

    def __setup_connections(self) -> None:
        self.psb_go_to_main_menu.clicked.connect(self.go_to_main_menu)
    #     self.psb_create_sheets.clicked.connect(self.create_sheets)
    #     self.psb_create_protocols.clicked.connect(self.create_protocols)

    def go_to_main_menu(self) -> None:
        self.change_page_signal.emit(MainWindowPages.MAIN_MENU)

    # def create_sheets(self):
    #     self.pte_logs.appendPlainText('нажали кнопку создания рабочих ведомостей'.upper())
    #     self.change_page_signal.emit(MainWindowPages.REPORT_CREATION)

    # def create_protocols(self):
    #     self.pte_logs.appendPlainText('пока данный функционал в разработке'.upper())
