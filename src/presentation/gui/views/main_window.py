from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from src.shared.constants import QtStyleResources

from ..generated import ResourceLoader, Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, /) -> None:
        super().__init__()
        self.__init_content_view()

    def __init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_WINDOW_STYLE).load_style())
        self.resize(1280, 800)
        self.setWindowTitle("Рабочий помощник КИА")

    def add_widget(self, widget: QWidget) -> int:
        layout_widget = self.__get_widget_to_insert(widget)
        index = self.stackedWidget_windows.addWidget(layout_widget)
        return index

    def show_widget(self, index: int) -> None:
        self.stackedWidget_windows.setCurrentIndex(index)

    @staticmethod
    def __get_widget_to_insert(widget: QWidget) -> QWidget:
        layout = QVBoxLayout()
        layout.addWidget(widget)
        widget.setLayout(layout)
        return widget
