from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from src.gui.constants import QtStyleResources, ReportsViews
from src.gui.generated import Ui_ReportsWindowWidget
from src.utils.qt_recource_loader import ResourceLoader

from ...core.constants import PageStructure


class ReportsWindow(QtWidgets.QWidget, Ui_ReportsWindowWidget):
    back_main_menu_signal = Signal()
    open_divisions_view_signal = Signal()
    open_staff_view_signal = Signal()
    open_work_types_view_signal = Signal()
    open_orders_view_signal = Signal()
    open_works_view_signal = Signal()
    open_work_events_view_signal = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.company = "Кубанское ПМЭС"
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
        self.comboBox_company.insertItem(0, self.company)

    def __setup_connections(self) -> None:
        self.pushButton_go_to_main_menu.clicked.connect(self.back_main_menu_signal.emit)
        self.pushButton_divisions.clicked.connect(self.open_divisions_view_signal.emit)
        self.pushButton_staff.clicked.connect(self.open_staff_view_signal.emit)
        self.pushButton_work_types.clicked.connect(self.open_work_types_view_signal.emit)
        self.pushButton_works.clicked.connect(self.open_works_view_signal.emit)
        self.pushButton_orders.clicked.connect(self.open_orders_view_signal.emit)
        self.pushButton_work_events.clicked.connect(self.open_work_events_view_signal.emit)

    def add_view(self, index: PageStructure, widget: QtWidgets.QWidget) -> None:
        layout_widget = self.get_widget_to_insert(widget)
        self.stackedWidget_report_types.insertWidget(index, layout_widget)

    def change_view(self, index: int) -> None:
        self.stackedWidget_report_types.setCurrentIndex(index)

    def _get_report_buttons_group(self) -> list[tuple[QtWidgets.QPushButton, int]]:
        return [
            (self.pushButton_divisions, ReportsViews.DIVISIONS),
            (self.pushButton_staff, ReportsViews.STAFF),
            (self.pushButton_work_types, ReportsViews.WORK_TYPES),
            (self.pushButton_works, ReportsViews.WORKS),
            (self.pushButton_orders, ReportsViews.ORDERS),
            (self.pushButton_work_events, ReportsViews.WORK_EVENTS),
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
