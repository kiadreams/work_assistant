from dishka import Container

from src.core.interfaces.ui import ReportsWindowViewProtocol
from src.gui.constants import ReportsWindowPages
from src.gui.views import (
    DivisionReportView,
    StaffReportView,
    WorkTypeReportView,
    WorkReportView,
    WorkEventReportView,
    OrderReportView,
)


class ReportsCoordinator:
    def __init__(self, reports_window: ReportsWindowViewProtocol, container: Container) -> None:
        self.reports_window = reports_window
        self.session_container = container

    def start_report_session(self) -> None:
        self.reports_window.insert_into_stacked_windows(
            ReportsWindowPages.DIVISIONS, self.session_container.get(DivisionReportView)
        )
        self.reports_window.insert_into_stacked_windows(
            ReportsWindowPages.STAFF, self.session_container.get(StaffReportView)
        )
        self.reports_window.insert_into_stacked_windows(
            ReportsWindowPages.WORK_TYPES, self.session_container.get(WorkTypeReportView)
        )
        self.reports_window.insert_into_stacked_windows(
            ReportsWindowPages.WORKS, self.session_container.get(WorkReportView)
        )
        self.reports_window.insert_into_stacked_windows(
            ReportsWindowPages.ORDERS, self.session_container.get(OrderReportView)
        )
        self.reports_window.insert_into_stacked_windows(
            ReportsWindowPages.WORK_EVENTS, self.session_container.get(WorkEventReportView)
        )
        self.reports_window.change_page(ReportsWindowPages.DIVISIONS)

    def open_main_menu_window(self) -> None:
        pass

    def open_division_window(self) -> None:
        pass

    def open_employee_window(self) -> None:
        pass

    def open_work_type_window(self) -> None:
        pass

    def open_work_window(self) -> None:
        pass

    def open_order_window(self) -> None:
        pass

    def open_work_event_window(self) -> None:
        pass
