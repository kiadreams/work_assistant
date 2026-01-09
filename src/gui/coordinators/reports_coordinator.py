from src.gui.constants import ReportsViews as Views
from src.gui.models.division_table_model import DivisionTableModel
from src.gui.views import (
    DivisionReportView,
    OrderReportView,
    ReportsWindow,
    StaffReportView,
    WorkEventReportView,
    WorkReportView,
    WorkTypeReportView,
)
from src.services.interfaces.services import EmployeeServiceProtocol
from src.viewmodels import DivisionViewModel


class ReportsCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service
        self._reports_window = ReportsWindow()

    @property
    def session_window(self) -> ReportsWindow:
        return self._reports_window

    def start_session(self) -> None:
        self._connect_signals()
        self.open_divisions_view()

    def _connect_signals(self) -> None:
        self.session_window.open_divisions_view_signal.connect(self.open_divisions_view)
        self.session_window.open_staff_view_signal.connect(self.open_staff_view)
        self.session_window.open_works_view_signal.connect(self.open_works_view)
        self.session_window.open_work_events_view_signal.connect(self.open_work_events_view)
        self.session_window.open_work_types_view_signal.connect(self.open_work_types_view)
        self.session_window.open_orders_view_signal.connect(self.open_orders_view)

    def open_divisions_view(self) -> None:
        print("Opening Divisions View")
        division_viewmodel = DivisionViewModel(self.employee_service)
        division_table_model = DivisionTableModel(division_viewmodel)
        division_view = DivisionReportView(division_table_model)
        self.session_window.add_view(Views.DIVISIONS, division_view)
        self.session_window.change_view(Views.DIVISIONS)

    def open_staff_view(self) -> None:
        print("Opening Staff View")
        self.session_window.add_view(Views.STAFF, StaffReportView())
        self.session_window.change_view(Views.STAFF)

    def open_work_types_view(self) -> None:
        print("Opening Work Types View")
        self.session_window.add_view(Views.WORK_TYPES, WorkTypeReportView())
        self.session_window.change_view(Views.WORK_TYPES)

    def open_works_view(self) -> None:
        print("Opening Works View")
        self.session_window.add_view(Views.WORKS, WorkReportView())
        self.session_window.change_view(Views.WORKS)

    def open_orders_view(self) -> None:
        print("Opening Orders View")
        self.session_window.add_view(Views.ORDERS, OrderReportView())
        self.session_window.change_view(Views.ORDERS)

    def open_work_events_view(self) -> None:
        print("Opening Work Events View")
        self.session_window.add_view(Views.WORK_EVENTS, WorkEventReportView())
        self.session_window.change_view(Views.WORK_EVENTS)
