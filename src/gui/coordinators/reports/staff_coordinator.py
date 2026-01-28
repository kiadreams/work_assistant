from src.core.services import EmployeeService
from src.gui.views.reports import StaffReportView


class StaffCoordinator:
    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service
        self._view = StaffReportView()

    def start(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> StaffReportView:
        return self._view

    def _connect_signals(self) -> None:
        pass

    def teardown(self) -> None:
        pass
