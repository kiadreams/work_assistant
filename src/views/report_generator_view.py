from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from ..utils.qt_recource_loader import ResourceLoader
from .order_report_view import OrderReportView
from .division_report_view import DivisionReportView
from .staff_report_view import StaffReportView
from .work_event_report_view import WorkEventReportView
from .work_report_view import WorkReportView
from .work_type_report_view import WorkTypeReportView
from ..constants import QtStyleResources
from ..constants import MainWindowPages, ReportGenerationPages
from .generated.ui.ui_report_generation_widget import Ui_ReportGenerationWidget
from ..view_models.division_viewmodel import DivisionViewModel


class ReportGeneratorView(QtWidgets.QWidget, Ui_ReportGenerationWidget):

    change_page_signal = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        self.services = DivisionReportView(DivisionViewModel("Кубансое ПМЭС"))
        self.staff = StaffReportView()
        self.work_types = WorkTypeReportView()
        self.works = WorkReportView()
        self.orders = OrderReportView()
        self.work_events = WorkEventReportView()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(
            ResourceLoader(QtStyleResources.REPORT_GENERATION_WIDGET_STYLE).load_style()
        )
        self.stackedWidget_report_types.insertWidget(
            ReportGenerationPages.SERVICES_AND_GROUPS, self.get_widget_to_insert(self.services)
        )
        self.stackedWidget_report_types.insertWidget(
            ReportGenerationPages.STAFF, self.get_widget_to_insert(self.staff)
        )
        self.stackedWidget_report_types.insertWidget(
            ReportGenerationPages.TYPES_OF_WORK, self.get_widget_to_insert(self.work_types)
        )
        self.stackedWidget_report_types.insertWidget(
            ReportGenerationPages.WORKS, self.get_widget_to_insert(self.works)
        )
        self.stackedWidget_report_types.insertWidget(
            ReportGenerationPages.ORDERS, self.get_widget_to_insert(self.orders)
        )
        self.stackedWidget_report_types.insertWidget(
            ReportGenerationPages.WORK_EVENTS, self.get_widget_to_insert(self.work_events)
        )

        self.reports_button_group = self.create_button_group(
            "reports_button_group", self.__get_elements_for_reports_button_group()
        )

        self.stackedWidget_report_types.setCurrentIndex(ReportGenerationPages.SERVICES_AND_GROUPS)
        self.pushButton_divisions.setChecked(True)

    def __setup_connections(self) -> None:
        self.pushButton_go_to_main_menu.clicked.connect(self.go_to_main_menu)
        self.reports_button_group.idClicked.connect(self.change_report_page)

    def change_report_page(self, index: int) -> None:
        self.stackedWidget_report_types.setCurrentIndex(index)

    def go_to_main_menu(self) -> None:
        self.change_page_signal.emit(MainWindowPages.MAIN_MENU)

    def __get_elements_for_reports_button_group(self) -> list[tuple[QtWidgets.QPushButton, int]]:
        return [
            (self.pushButton_divisions, ReportGenerationPages.SERVICES_AND_GROUPS),
            (self.pushButton_staff, ReportGenerationPages.STAFF),
            (self.pushButton_work_types, ReportGenerationPages.TYPES_OF_WORK),
            (self.pushButton_works, ReportGenerationPages.WORKS),
            (self.pushButton_orders, ReportGenerationPages.ORDERS),
            (self.pushButton_work_events, ReportGenerationPages.WORK_EVENTS),
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
