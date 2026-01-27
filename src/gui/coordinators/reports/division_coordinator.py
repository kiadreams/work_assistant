from __future__ import annotations

from typing import TYPE_CHECKING

from dependency_injector.providers import Factory

from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain
from src.gui.viewmodels import DivisionViewModel
from src.gui.views.dialogs.division_dialog_views import BaseDialogView
from src.gui.views.reports import DivisionReportView

if TYPE_CHECKING:
    from src.di.report_container import DivisionDialogContainer
    from src.gui.viewmodels.dialogs.base_dialog_model import BaseDialogViewModel


class DivisionsCoordinator:
    def __init__(
        self,
        division_viewmodel: DivisionViewModel,
        division_report_view: DivisionReportView,
        division_dialog_factory: Factory[DivisionDialogContainer],
    ) -> None:
        self._vm = division_viewmodel
        self._view = division_report_view
        self._division_dialog_factory = division_dialog_factory
        self._dialog_vm: BaseDialogViewModel | None = None
        self._dialog_view: BaseDialogView | None = None

    @property
    def view(self) -> DivisionReportView:
        return self._view

    def start(self) -> None:
        self._connect_signals()
        self._vm.init_model_data()
        self._view.init_content_view()

    def _connect_signals(self) -> None:
        self._view.add_new_division_signal.connect(self._handle_add_new_division_button)
        self._view.delete_division_signal.connect(self._vm.delete_current_division)
        self._view.edit_division_signal.connect(self._handle_edit_division_button)
        self._view.add_new_department_signal.connect(self._handle_add_new_department_button)
        self._view.delete_department_signal.connect(self._vm.delete_current_department)
        self._view.edit_department_signal.connect(self._handle_edit_department_button)

    def _disconnect_signals(self) -> None:
        self._view.add_new_division_signal.disconnect(self._handle_add_new_division_button)
        self._view.delete_division_signal.disconnect(self._vm.delete_current_division)
        self._view.edit_division_signal.disconnect(self._handle_edit_division_button)
        self._view.add_new_department_signal.disconnect(self._handle_add_new_department_button)
        self._view.delete_department_signal.disconnect(self._vm.delete_current_department)
        self._view.edit_department_signal.disconnect(self._handle_edit_department_button)

    def _handle_add_new_division_button(self) -> None:
        dialog = self._division_dialog_factory()
        self._dialog_vm = dialog.add_division_dialog_model()
        self._dialog_view = dialog.add_division_dialog_view()

        self._dialog_view.init_content_view()

        self._dialog_vm.close_view_with_data_signal.connect(self._close_add_division_dialog)
        self._dialog_vm.error_generation_signal.connect(self._dialog_view.show_warning_massage)
        self._dialog_view.data_accepted_signal.connect(self._dialog_vm.validate_data_dialog)

        self._dialog_vm.init_model_data()
        self._dialog_view.exec()

        self._dialog_vm.close_view_with_data_signal.disconnect(self._close_add_division_dialog)
        self._dialog_vm.error_generation_signal.disconnect(self._dialog_view.show_warning_massage)
        self._dialog_view.data_accepted_signal.disconnect(self._dialog_vm.validate_data_dialog)
        self._dialog_view.deleteLater()

    def _handle_edit_division_button(self) -> None:
        dialog = self._division_dialog_factory()
        self._dialog_vm = dialog.edit_division_dialog_model()
        self._dialog_view = dialog.edit_division_dialog_view()

        self._dialog_view.init_content_view()

        self._dialog_vm.set_view_data_signal.connect(self._dialog_view.set_view_data)
        self._dialog_vm.close_view_with_data_signal.connect(self._close_edit_division_dialog)
        self._dialog_vm.error_generation_signal.connect(self._dialog_view.show_warning_massage)
        self._dialog_view.data_accepted_signal.connect(self._dialog_vm.validate_data_dialog)

        self._dialog_vm.init_model_data()
        self._dialog_view.exec()

        self._dialog_vm.set_view_data_signal.disconnect(self._dialog_view.set_view_data)
        self._dialog_vm.close_view_with_data_signal.disconnect(self._close_edit_division_dialog)
        self._dialog_vm.error_generation_signal.disconnect(self._dialog_view.show_warning_massage)
        self._dialog_view.data_accepted_signal.disconnect(self._dialog_vm.validate_data_dialog)
        self._dialog_view.deleteLater()

    def _handle_add_new_department_button(self) -> None:
        dialog = self._division_dialog_factory()
        self._dialog_vm = dialog.add_department_dialog_model()
        self._dialog_view = dialog.add_department_dialog_view()

        self._dialog_view.init_content_view()

        self._dialog_vm.close_view_with_data_signal.connect(self._close_add_department_dialog)
        self._dialog_vm.error_generation_signal.connect(self._dialog_view.show_warning_massage)
        self._dialog_view.data_accepted_signal.connect(self._dialog_vm.validate_data_dialog)

        self._dialog_vm.init_model_data()
        self._dialog_view.exec()

        self._dialog_vm.close_view_with_data_signal.disconnect(self._close_add_department_dialog)
        self._dialog_vm.error_generation_signal.disconnect(self._dialog_view.show_warning_massage)
        self._dialog_view.data_accepted_signal.disconnect(self._dialog_vm.validate_data_dialog)
        self._dialog_view.deleteLater()

    def _handle_edit_department_button(self) -> None:
        dialog = self._division_dialog_factory()
        self._dialog_vm = dialog.edit_department_dialog_model()
        self._dialog_view = dialog.edit_department_dialog_view()

        self._dialog_view.init_content_view()

        self._dialog_vm.set_view_data_signal.connect(self._dialog_view.set_view_data)
        self._dialog_vm.close_view_with_data_signal.connect(self._close_edit_department_dialog)
        self._dialog_vm.error_generation_signal.connect(self._dialog_view.show_warning_massage)
        self._dialog_view.data_accepted_signal.connect(self._dialog_vm.validate_data_dialog)

        self._dialog_vm.init_model_data()
        self._dialog_view.exec()

        self._dialog_vm.set_view_data_signal.disconnect(self._dialog_view.set_view_data)
        self._dialog_vm.close_view_with_data_signal.disconnect(self._close_edit_department_dialog)
        self._dialog_vm.error_generation_signal.disconnect(self._handle_operation_error)
        self._dialog_view.data_accepted_signal.disconnect(self._dialog_vm.validate_data_dialog)
        self._dialog_view.deleteLater()

    def _close_add_division_dialog(self, division: DivisionDomain) -> None:
        self._vm.add_new_division(division)
        if self._dialog_view:
            self._dialog_view.accept()

    def _close_edit_division_dialog(self, division: DivisionDomain) -> None:
        self._vm.edit_current_division(division)
        if self._dialog_view:
            self._dialog_view.accept()

    def _close_add_department_dialog(self, department: DepartmentDomain) -> None:
        self._vm.add_new_department(department)
        if self._dialog_view:
            self._dialog_view.accept()

    def _close_edit_department_dialog(self, department: DepartmentDomain) -> None:
        self._vm.edit_current_department(department)
        if self._dialog_view:
            self._dialog_view.accept()

    def _handle_operation_error(self, title: str, message: str) -> None:
        if self._dialog_view:
            self._dialog_view.show_warning_massage(title, message)
        self.view.show_warning_massage(title, message)

    def teardown(self) -> None:
        self._disconnect_signals()
