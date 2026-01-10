from PySide6.QtWidgets import QWidget

from gui.interfaces.views import BaseViewProtocol
from gui.views import WorkReportView
from services.interfaces.services import EmployeeServiceProtocol


class WorksCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol):
        self.employee_service = employee_service
        self._view = WorkReportView

    def start_view(self) -> None:
        # self._view = DivisionReportView(self.table_model)
        self._connect_signals()

    @property
    def view(self) -> BaseViewProtocol | QWidget:
        return self._view

    def _connect_signals(self):
        pass
