from src.gui.views.reports import WorkTypeReportView
from core.interfaces.services import EmployeeServiceProtocol


class WorkTypesCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol):
        self.employee_service = employee_service
        self._view = WorkTypeReportView()

    def start_view(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> WorkTypeReportView:
        return self._view

    def _connect_signals(self) -> None:
        pass
