from PySide6 import QtWidgets

from .base_widgets import BaseAppWidgetMixin
from .main_menu import MainMenu
from .report_generator import ReportGenerator
from scripts.resource_loader import QtStyleResources
from ..windows.ui_main_window import Ui_MainWindow
from ..constants import MainWindowPages


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, BaseAppWidgetMixin):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = MainMenu()
        self.report_generator = ReportGenerator()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self._init_widget_style(QtStyleResources.MAIN_WINDOW_STYLE)
        self.stackedWidget_windows.insertWidget(
            MainWindowPages.MAIN_MENU, self.get_widget_to_insert(self.main_menu)
        )
        self.stackedWidget_windows.insertWidget(
            MainWindowPages.REPORT_CREATION, self.get_widget_to_insert(self.report_generator)
        )
        self.stackedWidget_windows.setCurrentIndex(MainWindowPages.MAIN_MENU)
        self.resize(1280, 800)

    def __setup_connections(self) -> None:
        self.main_menu.close_app_signal.connect(self.close)
        self.main_menu.change_page_signal.connect(self.change_page)
        self.report_generator.change_page_signal.connect(self.change_page)

    def change_page(self, index: int) -> None:
        self.stackedWidget_windows.setCurrentIndex(index)
