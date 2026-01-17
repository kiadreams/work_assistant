from src.gui.models.reports.division_report_table_models import (
    DivisionReportDepartmentTableModel,
    DivisionReportDivisionTableModel,
)
from src.gui.views import DialogEditView
from src.gui.views.dialogs.base_dialog_view import BaseDialogView
from src.gui.views.reports import DivisionReportView
from core.interfaces.services import EmployeeServiceProtocol
from src.viewmodels import DivisionViewModel


class DivisionsCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service
        self.vm = DivisionViewModel(self.employee_service)
        self.division_table_model = DivisionReportDivisionTableModel(self.vm)
        self.department_table_model = DivisionReportDepartmentTableModel(self.vm)
        self._view = DivisionReportView(self.division_table_model, self.department_table_model)
        self.dialog_view: BaseDialogView | None = None

    def start_view(self) -> None:
        self._connect_signals()
        self.vm.init_model_data()
        self._view.init_content_view()

    @property
    def view(self) -> DivisionReportView:
        return self._view

    def _connect_signals(self) -> None:
        self.view.add_new_division_signal.connect(self.handle_add_new_division_button)

    def handle_add_new_division_button(self) -> None:
        self.dialog_view = DialogEditView(self._view)
        self.dialog_view.initContentWidget()
        self.dialog_view.exec()
