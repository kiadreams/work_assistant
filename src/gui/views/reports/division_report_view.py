from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHeaderView

from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_DivisionReportWidget
from src.gui.models.reports.division_report_table_models import (
    DivisionReportDepartmentTableModel,
    DivisionReportDivisionTableModel,
)
from src.gui.views.base_views import BaseView
from src.utils.qt_recource_loader import ResourceLoader


class DivisionReportView(BaseView, Ui_DivisionReportWidget):
    add_new_division_signal = Signal()
    edit_division_signal = Signal()
    delete_division_signal = Signal()
    add_new_department_signal = Signal()
    edit_department_signal = Signal()
    delete_department_signal = Signal()

    def __init__(
        self,
        division_table_model: DivisionReportDivisionTableModel,
        department_table_model: DivisionReportDepartmentTableModel,
    ) -> None:
        super().__init__()
        self.division_model = division_table_model
        self.department_model = department_table_model
        self.vm = department_table_model.vm

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.reload_division_combobox_items()
        self.reload_department_combobox_items()
        self.__setup_connections()

    def __setup_connections(self) -> None:
        self.pushButton_add_division.clicked.connect(self.add_new_division_signal.emit)
        self.pushButton_remove_division.clicked.connect(self.delete_division_signal.emit)
        self.pushButton_edit_division.clicked.connect(self.edit_division_signal.emit)
        self.pushButton_add_department.clicked.connect(self.add_new_department_signal.emit)
        self.pushButton_remove_department.clicked.connect(self.delete_department_signal.emit)
        self.pushButton_edit_department.clicked.connect(self.edit_department_signal.emit)
        self.pushButton_show_all_divisions.clicked.connect(self.show_all_divisions)
        self.pushButton_show_departments_of_division.clicked.connect(
            self.show_departments_of_division
        )

        self.comboBox_division_list.currentTextChanged.connect(self.handle_combobox_division_change)
        self.comboBox_department_list.currentTextChanged.connect(
            self.handle_combobox_department_change
        )

        self.vm.division_data_changed_signal.connect(self.reload_division_combobox_items)
        self.vm.department_data_changed_signal.connect(self.reload_department_combobox_items)

    def show_all_divisions(self) -> None:
        self.tableView_division_data_table.setModel(self.division_model)
        header = self.tableView_division_data_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def show_departments_of_division(self) -> None:
        self.tableView_division_data_table.setModel(self.department_model)
        header = self.tableView_division_data_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def handle_combobox_division_change(self, division_name: str) -> None:
        self.vm.change_current_division(division_name)

    def handle_combobox_department_change(self, department_name: str) -> None:
        self.vm.change_current_department(department_name)

    def update_button_delete_division_states(self) -> None:
        enabled = self.vm.can_delete_current_division
        self.pushButton_remove_division.setEnabled(enabled)

    def update_button_show_all_divisions_states(self) -> None:
        enabled = self.vm.can_show_all_divisions
        self.pushButton_show_all_divisions.setEnabled(enabled)

    def update_button_edit_division_states(self) -> None:
        enabled = self.vm.can_edit_current_division
        self.pushButton_edit_division.setEnabled(enabled)

    def update_button_delete_department_states(self) -> None:
        enable = self.vm.can_delete_current_department
        self.pushButton_remove_department.setEnabled(enable)

    def update_button_show_departments_of_division_states(self) -> None:
        enable = self.vm.can_show_departments_of_division
        self.pushButton_show_departments_of_division.setEnabled(enable)

    def update_button_edit_department_states(self) -> None:
        enable = self.vm.can_edit_current_department
        self.pushButton_edit_department.setEnabled(enable)

    def update_division_button_states(self) -> None:
        self.update_button_show_all_divisions_states()
        self.update_button_delete_division_states()
        self.update_button_edit_division_states()

    def update_department_button_states(self) -> None:
        self.update_button_show_departments_of_division_states()
        self.update_button_delete_department_states()
        self.update_button_edit_department_states()

    def reload_division_combobox_items(self) -> None:
        self.comboBox_division_list.blockSignals(True)
        division_names, current_division_name = self.vm.division_name_data
        self.comboBox_division_list.clear()
        self.comboBox_division_list.addItems(division_names)
        self.comboBox_division_list.setCurrentText(current_division_name)
        self.comboBox_division_list.blockSignals(False)
        self.update_division_button_states()

    def reload_department_combobox_items(self) -> None:
        self.comboBox_department_list.blockSignals(True)
        department_names, current_department_name = self.vm.department_name_data
        self.comboBox_department_list.clear()
        self.comboBox_department_list.addItems(department_names)
        self.comboBox_department_list.setCurrentText(current_department_name)
        self.comboBox_department_list.blockSignals(False)
        self.update_department_button_states()
