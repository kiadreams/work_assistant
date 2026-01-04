from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from src.utils.qt_recource_loader import ResourceLoader
from src.gui.constants import ReportsWindowPages, QtStyleResources
from src.gui.generated import Ui_ReportsWindowWidget
from ...core.constants import PageStructure


class ReportsWindowView(QtWidgets.QWidget, Ui_ReportsWindowWidget):

    back_main_menu_signal = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.init_content_view()
        self.reports_button_group = self.create_button_group(
            "reports_button_group", self._get_report_buttons_group()
        )
        self.__setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(
            ResourceLoader(QtStyleResources.REPORT_GENERATION_WIDGET_STYLE).load_style()
        )
        self.pushButton_divisions.setChecked(True)

    def insert_into_stacked_windows(self, index: PageStructure, widget: QtWidgets.QWidget) -> None:
        layout_widget = self.get_widget_to_insert(widget)
        self.stackedWidget_report_types.insertWidget(index, layout_widget)

    def __setup_connections(self) -> None:
        self.pushButton_go_to_main_menu.clicked.connect(self.back_main_menu_signal.emit)
        self.reports_button_group.idClicked.connect(self.change_page)

    def change_page(self, index: int) -> None:
        self.stackedWidget_report_types.setCurrentIndex(index)

    def _get_report_buttons_group(self) -> list[tuple[QtWidgets.QPushButton, int]]:
        return [
            (self.pushButton_divisions, ReportsWindowPages.DIVISIONS),
            (self.pushButton_staff, ReportsWindowPages.STAFF),
            (self.pushButton_work_types, ReportsWindowPages.WORK_TYPES),
            (self.pushButton_works, ReportsWindowPages.WORKS),
            (self.pushButton_orders, ReportsWindowPages.ORDERS),
            (self.pushButton_work_events, ReportsWindowPages.WORK_EVENTS),
        ]

    @staticmethod
    def get_widget_to_insert(widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        widget.setLayout(layout)
        return widget

    @staticmethod
    def create_button_group(
        name_group: str,
        elements: list[tuple[QtWidgets.QPushButton, int]],
        exclusive: bool = True,
    ) -> QtWidgets.QButtonGroup:
        button_group = QtWidgets.QButtonGroup()
        button_group.setExclusive(exclusive)
        for element in elements:
            button, index = element
            button.setCheckable(exclusive)
            button_group.addButton(button, index)
        button_group.setObjectName(name_group)
        return button_group
