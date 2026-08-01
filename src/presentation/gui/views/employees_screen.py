from __future__ import annotations

from typing import Any

from PySide6.QtCore import Signal
from PySide6.QtGui import QStandardItemModel

from src.presentation.view_dtos import DepartmentViewDto, DivisionViewDto, EmployeeViewDto
from src.shared.constants import QtStyleResources

from ..generated import Ui_EmployeesWidget
from .base_view import BaseView


class EmployeesScreen(BaseView, Ui_EmployeesWidget):
    to_main_menu_click_signal = Signal()
    add_employee_signal = Signal(dict[str, Any])
    delete_employee_signal = Signal(EmployeeViewDto)
    change_division_list_signal = Signal(DivisionViewDto)
    change_department_list_signal = Signal(DepartmentViewDto)
    change_employee_data_signal = Signal(EmployeeViewDto, dict[str, Any])

    def __init__(self) -> None:
        super().__init__()
        self._divisions_model = QStandardItemModel()
        self._departments_model = QStandardItemModel()
        self._init_content_view(QtStyleResources.REPORT_WIDGET_STYLE)

    def _view_customization(self) -> None:
        self.comboBox_division_list.setModel(self._divisions_model)
        self.comboBox_department_list.setModel(self._departments_model)

    def _setup_connections(self) -> None:
        self.pushButton_to_main_menu.clicked.connect(self.to_main_menu_click_signal.emit)
        self.pushButton_delete_employee.clicked.connect(self._delete_employees)
        self.pushButton_add_employee.clicked.connect(self._add_employee)
        self.comboBox_division_list.currentIndexChanged.connect(self._change_division_list)
        self.comboBox_department_list.currentIndexChanged.connect(self._change_department_list)

    def _delete_employees(self) -> None:
        print("delete employee list")
        pass

    def _add_employee(self) -> None:
        print("add employee")
        pass

    def _set_all_departments(self, departments: list[dict]) -> None:
        self.comboBox_department_list.blockSignals(True)
        self._departments_model.clear()
        pass

    def _set_all_divisions(self) -> None:
        pass

    def _change_division_list(self) -> None:
        print("change division list")
        pass

    def _change_department_list(self) -> None:
        print("change department list")
        pass

