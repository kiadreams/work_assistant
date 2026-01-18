from src.core.interfaces.services import EmployeeServiceProtocol
from src.core.models.division_domain import DivisionDomain
from src.gui.models.reports.division_report_table_models import (
    DivisionReportDepartmentTableModel,
    DivisionReportDivisionTableModel,
)
from src.gui.viewmodels import DivisionViewModel
from src.gui.views import DialogAddDivision
from src.gui.views.dialogs.dialog_views import BaseDialogView
from src.gui.views.reports import DivisionReportView


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
        self.dialog_view = DialogAddDivision(self._view)
        self.dialog_view.init_content_widget()
        self.dialog_view.buttonBox_exit.accepted.connect(self.validate_new_division)
        self.dialog_view.exec()
        self.dialog_view.buttonBox_exit.accepted.disconnect(self.validate_new_division)

    def validate_new_division(self) -> None:
        if self.dialog_view:
            division_dto = self.dialog_view.get_data()
            if division_dto:
                division = DivisionDomain.division_from_data(division_dto)
                print(division)
                self.dialog_view.accept()
