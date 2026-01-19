from pydantic import ValidationError
from PySide6.QtWidgets import QMessageBox

from src.core.interfaces.services import EmployeeServiceProtocol
from src.core.models.division_domain import DivisionDomain
from src.gui.dto.models import DivisionDto
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
        if self.dialog_view.exec():
            self.vm.add_new_division()
        self.dialog_view.buttonBox_exit.accepted.disconnect(self.validate_new_division)
        self.dialog_view = None
        print(f"удаляем экземпляр диалога: {self.dialog_view}")

    def validate_new_division(self) -> None:
        if not self.dialog_view:
            return None
        division_dto = None
        try:
            division_dto = DivisionDto.model_validate(self.dialog_view.get_data())
        except ValidationError as e:
            field = e.errors()[0]["loc"][0]
            match field:
                case "name":
                    text = "Укажите правильно название службы"
            QMessageBox.warning(
                self.dialog_view,
                "Ошибка формата данных",
                f"Некорректно указаны данные: \n{text}",
            )
        if not division_dto:
            return None
        division = DivisionDomain.division_from_data(division_dto)
        if self.vm.check_division(division):
            self.dialog_view.accept()
        else:
            QMessageBox.warning(
                self.dialog_view,
                "Ошибка данных",
                "Служба с таким наименованием уже существует...",
            )
        return None
