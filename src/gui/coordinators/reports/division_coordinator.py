from PySide6.QtWidgets import QWidget

from gui.interfaces.views import BaseViewProtocol
from gui.models.reports.division_table_model import DivisionTableModel
from gui.views import DivisionReportView
from services.interfaces.services import EmployeeServiceProtocol
from viewmodels import DivisionViewModel


class DivisionsCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service
        self.vm = DivisionViewModel(self.employee_service)
        self.table_model = DivisionTableModel(self.vm)
        self._view = DivisionReportView(self.table_model)

    def start_view(self) -> None:
        # self._view = DivisionReportView(self.table_model)
        self._connect_signals()

    @property
    def view(self) -> BaseViewProtocol | QWidget:
        return self._view

    def _connect_signals(self):
        self._view.show_all_divisions_signal.connect(self.handle_show_divisions)
        self._view.show_all_departments_signal.connect(self.handle_show_departments)

    def handle_show_divisions(self) -> None:
        self._view.show_all_divisions()

    def handle_show_departments(self) -> None:
        print("Отображаем таблицу отделов")
        self._view.show_all_departments()
