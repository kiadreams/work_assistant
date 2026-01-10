from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHeaderView

from gui.models.reports.division_table_model import DivisionTableModel
from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_DivisionReportWidget
from src.utils.qt_recource_loader import ResourceLoader


class DivisionReportView(QtWidgets.QWidget, Ui_DivisionReportWidget):
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
        self.init_content_view()
        self.__setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.comboBox_division_list.setModel(self.division_model)
        self.comboBox_division_list.setModelColumn(1)

    def __setup_connections(self) -> None:
        self.pushButton_add_division.clicked.connect(self.add_new_division_signal.emit)
        self.pushButton_remove_division.clicked.connect(self.delete_division_signal.emit)
        self.pushButton_edit_division.clicked.connect(self.edit_division_signal.emit)
        self.pushButton_add_department.clicked.connect(self.add_new_department_signal.emit)
        self.pushButton_remove_department.clicked.connect(self.delete_department_signal.emit)
        self.pushButton_edit_department.clicked.connect(self.edit_department_signal.emit)
        self.pushButton_show_all_divisions.clicked.connect(self.show_all_divisions_signal.emit)
        self.pushButton_show_all_department.clicked.connect(self.show_all_departments_signal.emit)

    def show_all_divisions(self) -> None:
        self.tableView_division_data_table.setModel(self.division_model)
        header = self.tableView_division_data_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def show_all_departments(self) -> None:
        pass