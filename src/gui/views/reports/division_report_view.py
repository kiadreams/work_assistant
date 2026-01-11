from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHeaderView

from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_DivisionReportWidget
from src.gui.models.reports.division_table_model import DivisionTableModel
from src.gui.views.base_views import BaseView
from src.utils.qt_recource_loader import ResourceLoader


class DivisionReportView(BaseView, Ui_DivisionReportWidget):
    add_new_division_signal = Signal()
    edit_division_signal = Signal()
    delete_division_signal = Signal()
    show_all_divisions_signal = Signal()
    add_new_department_signal = Signal()
    edit_department_signal = Signal()
    delete_department_signal = Signal()
    show_all_departments_signal = Signal()

    def __init__(self, table_model: DivisionTableModel) -> None:
        super().__init__()
        self.division_model = table_model

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.comboBox_division_list.setModel(self.division_model)
        self.comboBox_division_list.setModelColumn(1)
        self.__setup_connections()

    def __setup_connections(self) -> None:
        self.pushButton_add_division.clicked.connect(self.add_new_division_signal.emit)
        self.pushButton_remove_division.clicked.connect(self.delete_division_signal.emit)
        self.pushButton_edit_division.clicked.connect(self.edit_division_signal.emit)
        self.pushButton_add_department.clicked.connect(self.add_new_department_signal.emit)
        self.pushButton_remove_department.clicked.connect(self.delete_department_signal.emit)
        self.pushButton_edit_department.clicked.connect(self.edit_department_signal.emit)
        self.pushButton_show_all_divisions.clicked.connect(self.show_all_divisions_signal.emit)
        self.pushButton_show_all_department.clicked.connect(self.show_all_departments_signal.emit)

        self.comboBox_division_list.currentTextChanged.connect(self.handle_combobox_division_change)

        self.division_model.vm.change_current_division_signal.connect(self.set_current_division)

    def show_all_divisions(self) -> None:
        self.tableView_division_data_table.setModel(self.division_model)
        header = self.tableView_division_data_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def show_all_departments(self) -> None:
        pass

    def handle_combobox_division_change(self, division_name: str) -> None:
        self.division_model.vm.change_current_division(division_name)

    def set_current_division(self) -> None:
        current_division = self.division_model.vm.current_division
        if current_division:
            self.comboBox_division_list.blockSignals(True)
            self.comboBox_division_list.setCurrentText(current_division.name)
            self.comboBox_division_list.blockSignals(False)
        self.update_button_states()

    def update_button_delete_division_states(self) -> None:
        enabled = self.division_model.vm.can_delete_current_division
        self.pushButton_remove_division.setEnabled(enabled)

    def update_button_show_all_divisions_states(self) -> None:
        enabled = self.division_model.vm.can_show_all_divisions
        self.pushButton_show_all_divisions.setEnabled(enabled)

    def update_button_edit_division_states(self) -> None:
        enabled = self.division_model.vm.can_edit_current_division
        self.pushButton_edit_division.setEnabled(enabled)

    def update_button_delete_department_states(self) -> None:
        pass

    def update_button_show_all_department_states(self) -> None:
        pass

    def update_button_edit_department_states(self) -> None:
        pass

    def update_button_states(self) -> None:
        self.update_button_show_all_divisions_states()
        self.update_button_delete_division_states()
        self.update_button_edit_division_states()
        self.update_button_show_all_department_states()
        self.update_button_delete_department_states()
        self.update_button_edit_department_states()
