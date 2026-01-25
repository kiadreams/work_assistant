from __future__ import annotations

from typing import TYPE_CHECKING

from dependency_injector.providers import Factory

from src.core.models.division_domain import DivisionDomain
from src.gui.viewmodels import DivisionViewModel
from src.gui.viewmodels.dialogs.add_division_dialog_model import AddDivisionDialogModel
from src.gui.views.dialogs.base_dialog_view import BaseDialogView
from src.gui.views.reports import DivisionReportView

if TYPE_CHECKING:
    from src.di.report_container import DivisionDialogContainer


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
        self._current_dialog_vm: AddDivisionDialogModel | None = None
        self._current_dialog_view: BaseDialogView | None = None

    @property
    def view(self) -> DivisionReportView:
        return self._view

    def start(self) -> None:
        self._connect_signals()
        self._vm.init_model_data()
        self._view.init_content_view()

    def _connect_signals(self) -> None:
        self._view.add_new_division_signal.connect(self.handle_add_new_division_button)
        self._view.delete_division_signal.connect(self._vm.delete_current_division)
        self._view.edit_division_signal.connect(self.handle_edit_division_button)
        self._view.add_new_department_signal.connect(self.handle_add_new_department_button)
        self._view.delete_department_signal.connect(self._vm.delete_current_department)
        self._view.edit_department_signal.connect(self.handle_edit_department_button)

    def _disconnect_signals(self) -> None:
        self._view.add_new_division_signal.disconnect(self.handle_add_new_division_button)
        self._view.delete_division_signal.disconnect(self._vm.delete_current_division)
        self._view.edit_division_signal.disconnect(self.handle_edit_division_button)
        self._view.add_new_department_signal.disconnect(self.handle_add_new_department_button)
        self._view.delete_department_signal.disconnect(self._vm.delete_current_department)
        self._view.edit_department_signal.disconnect(self.handle_edit_department_button)

    def handle_add_new_division_button(self) -> None:
        dialog = self._division_dialog_factory()
        self._current_dialog_vm = dialog.add_division_dialog_model()
        self._current_dialog_view = dialog.add_division_dialog_view()
        self._connect_current_dialog_signals()
        self._current_dialog_view.exec()
        self._disconnect_current_dialog_signals()
        self._current_dialog_view.deleteLater()

    def handle_edit_division_button(self, division_name: str) -> None:
        dialog = self._division_dialog_factory()
        # self.
        print(f"Нажали править службу с текущим именем: {division_name}")

    def handle_add_new_department_button(self) -> None:
        print("Нажали добавить новый отдел...")

    def handle_edit_department_button(self, department_name: str) -> None:
        print(f"Нажали править отдел с текущим именем: {department_name}")

    def _connect_current_dialog_signals(self) -> None:
        if self._current_dialog_vm and self._current_dialog_view:
            self._current_dialog_view.init_content_widget()
            self._current_dialog_vm.show_error_signal.connect(
                self._current_dialog_view.show_warning_massage
            )
            self._current_dialog_view.data_accepted_signal.connect(
                self._current_dialog_vm.validate_accepted_data_dialog
            )
            self._current_dialog_vm.close_dialog_with_data_signal.connect(
                self._close_add_division_dialog
            )

    def _disconnect_current_dialog_signals(self) -> None:
        if self._current_dialog_vm and self._current_dialog_view:
            self._current_dialog_vm.show_error_signal.disconnect(
                self._current_dialog_view.show_warning_massage
            )
            self._current_dialog_view.data_accepted_signal.disconnect(
                self._current_dialog_vm.validate_accepted_data_dialog
            )
            self._current_dialog_vm.close_dialog_with_data_signal.disconnect(
                self._close_add_division_dialog
            )

    def _close_add_division_dialog(self, division: DivisionDomain) -> None:
        self._vm.add_new_division(division)
        if self._current_dialog_view:
            self._current_dialog_view.accept()

    def teardown(self) -> None:
        self._disconnect_signals()
