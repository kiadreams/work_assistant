from src.gui.views.reports import WorkEventReportView
from src.services.interfaces.services import EmployeeServiceProtocol


class WorkEventsCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol):
        self.employee_service = employee_service
        self._view = WorkEventReportView()

    def start_view(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> WorkEventReportView:
        return self._view

    def _connect_signals(self) -> None:
        pass
