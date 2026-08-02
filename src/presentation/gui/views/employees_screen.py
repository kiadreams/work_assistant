from __future__ import annotations

from typing import TYPE_CHECKING, Any

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QHeaderView

from src.presentation.view_dtos import DepartmentViewDto, DivisionViewDto, EmployeeViewDto
from src.shared.constants import QtStyleResources

from ..generated import Ui_EmployeesWidget
from .ui_components import BaseView, TypedStandardItem

if TYPE_CHECKING:
    from src.presentation.gui.models.epmpoyee_table_model import EmployeeTableModel


class EmployeesScreen(BaseView, Ui_EmployeesWidget):
    to_main_menu_signal = Signal()
    employee_addition_signal = Signal(dict[str, Any])
    employee_removal_signal = Signal(EmployeeViewDto)
    division_list_changed_signal = Signal(DivisionViewDto)
    show_division_employees_signal = Signal(DivisionViewDto)
    show_department_employees_signal = Signal(DepartmentViewDto)
    employee_data_changed_signal = Signal(EmployeeViewDto, dict[str, Any])
    clear_employee_table_signal = Signal()

    def __init__(self, employee_table_model: EmployeeTableModel) -> None:
        super().__init__()
        self._employee_model = employee_table_model
        self._division_model = QStandardItemModel()
        self._department_model = QStandardItemModel()
        self._init_content_view(QtStyleResources.REPORT_WIDGET_STYLE)

    def _view_customization(self) -> None:
        self.division_list.setModel(self._division_model)
        self.department_list.setModel(self._department_model)
        self.employee_data_table.setModel(self._employee_model)

        header = self.employee_data_table.horizontalHeader()
        header.setStretchLastSection(False)  # Отключаем автодобор для последней колонки
        # 1. Задаем режимы изменения размеров
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # №
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)  # Дата рождения
        # Внутренние колонки переводим в Interactive, чтобы ими можно было управлять из кода
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # ФИО
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Должность
        # Задаем базовые размеры для фиксированных колонок
        header.resizeSection(0, 35)
        header.resizeSection(3, 100)

        # 2. Функция динамического пересчета пропорций 5 к 2
        def adjust_column_proportions() -> None:
            total_width = self.employee_data_table.width()
            # Вычитаем ширину фиксированных колонок (35 + 100) и рамки таблицы (~5)
            available_width = total_width - 35 - 100 - 5

            if available_width > 0:
                one_part = available_width / 10  # 7 + 3 = 7 частей
                # Принудительно выставляем размеры по весам
                header.resizeSection(1, int(one_part * 7))  # 5 частей под ФИО
                header.resizeSection(2, int(one_part * 3))  # 2 части под Должность

        # 3. Привязываем пересчет к изменению геометрии таблицы.
        # Этот сигнал срабатывает ВСЕГДА: при старте, при максимизации окна, при ресайзе мышкой.
        header.geometriesChanged.connect(adjust_column_proportions)
        # Вызываем один раз вручную для первичной отрисовки при старте
        adjust_column_proportions()

        # Поведение таблицы (остальные ваши настройки)
        self.employee_data_table.setWordWrap(True)
        self.employee_data_table.setSelectionBehavior(
            self.employee_data_table.SelectionBehavior.SelectRows
        )
        self.employee_data_table.setEditTriggers(
            self.employee_data_table.editTriggers().NoEditTriggers
        )
        self.employee_data_table.setSelectionMode(
            self.employee_data_table.SelectionMode.SingleSelection
        )

    def _setup_connections(self) -> None:
        self.to_main_menu_btn.clicked.connect(self.to_main_menu_signal.emit)
        self.delete_employee_btn.clicked.connect(self._delete_employees)
        self.add_employee_btn.clicked.connect(self._add_employee)
        self.division_list.currentIndexChanged.connect(self._change_division_list)
        self.department_list.currentIndexChanged.connect(self._change_department_list)

    def _delete_employees(self) -> None:
        print("delete employee list")
        pass

    def _add_employee(self) -> None:
        print("add employee")
        pass

    def set_employees_data(self, employees: list[EmployeeViewDto]) -> None:
        self._employee_model.set_employees(employees)
        self.employee_data_table.resizeRowsToContents()

    def set_division_departments(self, departments: list[DepartmentViewDto] | None = None) -> None:
        self.department_list.blockSignals(True)
        try:
            self._department_model.clear()
            if departments:
                item = TypedStandardItem[None]("Персонал службы")
                self._department_model.appendRow(item)
                for department in departments:
                    item = TypedStandardItem[DepartmentViewDto](department.display_name)
                    item.dto = department
                    self._department_model.appendRow(item)
            else:
                item = TypedStandardItem[None]("Отделов нет")
                item.setFlags(Qt.ItemFlag.ItemIsSelectable)
                self._department_model.appendRow(item)
            self.department_list.setCurrentIndex(0)
        finally:
            self.department_list.blockSignals(False)
        self._change_department_list()

    def set_company_divisions(self, divisions: list[DivisionViewDto] | None = None) -> None:
        self.division_list.blockSignals(True)
        try:
            self._division_model.clear()
            if divisions:
                for division in divisions:
                    item = TypedStandardItem[DivisionViewDto](division.display_name)
                    item.dto = division
                    self._division_model.appendRow(item)
            else:
                item = TypedStandardItem[None]("Служб нет")
                item.setFlags(Qt.ItemFlag.ItemIsSelectable)
                self._division_model.appendRow(item)
            self.division_list.setCurrentIndex(0)
        finally:
            self.division_list.blockSignals(False)
        self._change_division_list()

    def _change_division_list(self) -> None:
        division_index = self.division_list.view().currentIndex()
        division_item = self._division_model.itemFromIndex(division_index)
        if hasattr(division_item, "dto"):
            self.division_list_changed_signal.emit(division_item.dto)
        else:
            self.set_division_departments()

    def _change_department_list(self) -> None:
        department_index = self.department_list.view().currentIndex()
        department_item = self._department_model.itemFromIndex(department_index)
        if hasattr(department_item, "dto"):
            self.show_department_employees_signal.emit(department_item.dto)
            return
        division_index = self.division_list.view().currentIndex()
        division_item = self._division_model.itemFromIndex(division_index)
        if hasattr(division_item, "dto"):
            self.show_division_employees_signal.emit(division_item.dto)
        else:
            self.clear_employee_table_signal.emit()
