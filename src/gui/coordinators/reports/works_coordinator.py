from src.gui.views.reports import WorkReportView
from core.interfaces.services import EmployeeServiceProtocol


class WorksCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol):
        self.employee_service = employee_service
        self._view = WorkReportView()

    def start_view(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> WorkReportView:
        return self._view

    def _connect_signals(self) -> None:
        pass
