from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from src.core.constants import PageStructure, QtStyleResources
from src.gui.generated import Ui_MainWindow
from src.gui.utils import ResourceLoader


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, /) -> None:
        super().__init__()
        self.init_content_view()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_WINDOW_STYLE).load_style())
        self.resize(1280, 800)

    def add_window(self, index: PageStructure, widget: QWidget) -> None:
        layout_widget = self.get_widget_to_insert(widget)
        self.stackedWidget_windows.insertWidget(index, layout_widget)

    def change_window(self, index: int) -> None:
        self.stackedWidget_windows.setCurrentIndex(index)

    @staticmethod
    def get_widget_to_insert(widget: QWidget) -> QWidget:
        layout = QVBoxLayout()
        layout.addWidget(widget)
        widget.setLayout(layout)
        return widget
