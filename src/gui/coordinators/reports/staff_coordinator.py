from src.gui.views.reports import StaffReportView
from src.services.interfaces.services import EmployeeServiceProtocol


class StaffCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol):
        self.employee_service = employee_service
        self._view = StaffReportView()

    def start_view(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> StaffReportView:
        return self._view

    def _connect_signals(self) -> None:
        pass
