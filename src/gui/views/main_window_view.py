from PySide6 import QtWidgets

from src.utils.qt_recource_loader import ResourceLoader
from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_MainWindow
from ...core.constants import PageStructure


class MainWindowView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_content_view()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_WINDOW_STYLE).load_style())
        self.resize(1280, 800)

    def insert_into_stacked_windows(self, index: PageStructure, widget: QtWidgets.QWidget) -> None:
        layout_widget = self.get_widget_to_insert(widget)
        self.stackedWidget_windows.insertWidget(index, layout_widget)

    def change_page(self, index: int) -> None:
        self.stackedWidget_windows.setCurrentIndex(index)

    @staticmethod
    def get_widget_to_insert(widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        widget.setLayout(layout)
        return widget
