from src.gui.models.reports.division_table_model import DivisionTableModel
from src.gui.views.reports import DivisionReportView
from src.services.interfaces.services import EmployeeServiceProtocol
from src.viewmodels import DivisionViewModel


class DivisionsCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service
        self.vm = DivisionViewModel(self.employee_service)
        self.table_model = DivisionTableModel(self.vm)
        self._view = DivisionReportView(self.table_model)

    def start_view(self) -> None:
        self._connect_signals()
        self._view.init_content_view()
        self.vm.init_model_data()

    @property
    def view(self) -> DivisionReportView:
        return self._view

    def _connect_signals(self) -> None:
        self._view.show_all_divisions_signal.connect(self.handle_show_divisions)
        self._view.show_all_departments_signal.connect(self.handle_show_departments)

    def handle_show_divisions(self) -> None:
        self._view.show_all_divisions()

    def handle_show_departments(self) -> None:
        self._view.show_all_departments()
