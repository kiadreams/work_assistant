from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from . import base_widgets  # import QtWidgets, BaseAppWidgetMixin, BaseButtonGroupMixin,
from .order_reports import OrderReport
from .service_reports import ServiceReport
from .staff_reports import StaffReport
from .work_event_reports import WorkEventReport
from .work_reports import WorkReport
from .work_type_reports import WorkTypeReport
from ..constants import QtStyleResources
from ..constants import MainWindowPages, ReportGenerationPages
from ..windows.ui_report_generation_widget import Ui_ReportGenerationWidget
from src.view_models.view_service_models import ViewServiceModel


class ReportGenerator(
    QtWidgets.QWidget,
    Ui_ReportGenerationWidget,
    base_widgets.BaseAppWidgetMixin,
    base_widgets.BaseButtonGroupMixin,
):

    change_page_signal = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        self.services = ServiceReport(ViewServiceModel("Кубансое ПМЭС"))
        self.staff = StaffReport()
        self.work_types = WorkTypeReport()
        self.works = WorkReport()
        self.orders = OrderReport()
        self.work_events = WorkEventReport()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self._init_widget_style(QtStyleResources.REPORT_GENERATION_WIDGET_STYLE)
        self.stackedWidget_types_of_reports.insertWidget(
            ReportGenerationPages.SERVICES_AND_GROUPS, self.get_widget_to_insert(self.services)
        )
        self.stackedWidget_types_of_reports.insertWidget(
            ReportGenerationPages.STAFF, self.get_widget_to_insert(self.staff)
        )
        self.stackedWidget_types_of_reports.insertWidget(
            ReportGenerationPages.TYPES_OF_WORK, self.get_widget_to_insert(self.work_types)
        )
        self.stackedWidget_types_of_reports.insertWidget(
            ReportGenerationPages.WORKS, self.get_widget_to_insert(self.works)
        )
        self.stackedWidget_types_of_reports.insertWidget(
            ReportGenerationPages.ORDERS, self.get_widget_to_insert(self.orders)
        )
        self.stackedWidget_types_of_reports.insertWidget(
            ReportGenerationPages.WORK_EVENTS, self.get_widget_to_insert(self.work_events)
        )

        self.reports_button_group = self.create_button_group(
            "reports_button_group", self.__get_elements_for_reports_button_group()
        )

        self.stackedWidget_types_of_reports.setCurrentIndex(
            ReportGenerationPages.SERVICES_AND_GROUPS
        )
        self.pushButton_services.setChecked(True)

    def __setup_connections(self) -> None:
        self.pushButton_go_to_main_menu.clicked.connect(self.go_to_main_menu)
        self.reports_button_group.idClicked.connect(self.change_report_page)

    def change_report_page(self, index: int) -> None:
        self.stackedWidget_types_of_reports.setCurrentIndex(index)

    def go_to_main_menu(self) -> None:
        self.change_page_signal.emit(MainWindowPages.MAIN_MENU)

    def __get_elements_for_reports_button_group(self) -> list[tuple[QtWidgets.QPushButton, int]]:
        return [
            (self.pushButton_services, ReportGenerationPages.SERVICES_AND_GROUPS),
            (self.pushButton_staff, ReportGenerationPages.STAFF),
            (self.pushButton_work_types, ReportGenerationPages.TYPES_OF_WORK),
            (self.pushButton_works, ReportGenerationPages.WORKS),
            (self.pushButton_orders, ReportGenerationPages.ORDERS),
            (self.pushButton_work_events, ReportGenerationPages.WORK_EVENTS),
        ]
