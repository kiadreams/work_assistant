from typing import Callable

from PySide6 import QtWidgets
from PySide6.QtWidgets import QHeaderView

from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_DivisionReportWidget
from src.utils.qt_recource_loader import ResourceLoader

from ..models.division_table_model import DivisionTableModel
from .dialog_edit_view import DialogEditView


class DivisionReportView(QtWidgets.QWidget, Ui_DivisionReportWidget):
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
        # self.refresh_division_report()

    def __setup_connections(self) -> None:
        self.pushButton_add_division.clicked.connect(self.add_new_division)
        self.pushButton_remove_division.clicked.connect(self.remove_division)
        self.pushButton_edit_division.clicked.connect(self.edit_division)
        self.pushButton_add_department.clicked.connect(self.push_add_department)
        self.pushButton_remove_department.clicked.connect(self.push_remove_department)
        self.pushButton_edit_department.clicked.connect(self.push_edit_department)
        self.pushButton_show_all_divisions.clicked.connect(self.show_all_departments)

    def choose_current_division(self, service_name: str) -> None:
        # self.model.choose_current_division(service_name)
        # self.refresh_division_report()
        pass

    def refresh_division_report(self) -> None:
        self.refresh_combobox_division_list()
        self.check_enabled_division_deleted_button()

    def check_enabled_division_deleted_button(self) -> None:
        # is_enabled = self.model.is_current_division_deleted
        # self.pushButton_remove_division.setEnabled(is_enabled)
        pass

    def add_new_division(self) -> None:
        self.call_data_dialog()

    def remove_division(self) -> None:
        if self.division_model.is_current_division_deleted:
            self.ask_for_confirmation(
                f"Вы уверены, что хотите безвозвратно удалить службу {self.division_model.current_division}? "
                "Отменить это действие будет невозможно...",
                self.delete_current_division,
            )

    def edit_division(self) -> None:
        self.call_data_dialog()

    def show_all_departments(self) -> None:
        print("Показать таблицу")
        header = self.tableView_division_data_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)
        self.tableView_division_data_table.setModel(self.division_model)
        self.division_model.vm.load_all_divisions()

    def push_add_department(self) -> None:
        self.call_data_dialog()

    def push_remove_department(self) -> None:
        self.call_data_dialog()

    def push_edit_department(self) -> None:
        self.call_data_dialog()

    def call_data_dialog(self) -> None:
        dialog = DialogEditView(self)
        result = dialog.exec_()
        if result == DialogEditView.DialogCode.Accepted:
            pass
        else:
            pass

    def ask_for_confirmation(self, message_text: str, action: Callable[[], None]) -> None:
        reply = QtWidgets.QMessageBox.question(
            self,  # Родительский виджет (наше главное окно)
            "Подтверждение действия",  # Заголовок окна (Title bar)
            message_text,  # Текст сообщения
            QtWidgets.QMessageBox.StandardButton.Yes
            | QtWidgets.QMessageBox.StandardButton.No,  # Комбинация стандартных кнопок
            QtWidgets.QMessageBox.StandardButton.No,  # Кнопка по умолчанию (выделенная)
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Пользователь подтвердил действие. Выполняем удаление...")
            action()

    def delete_current_division(self) -> None:
        self.division_model.delete_current_division()
        self.refresh_division_report()

    def refresh_combobox_division_list(self) -> None:
        self.comboBox_division_list.blockSignals(True)
        self.comboBox_division_list.clear()
        self.comboBox_division_list.addItems([d.name for d in self.division_model.divisions])
        self.comboBox_division_list.setCurrentText(
            self.division_model.current_division.name if self.division_model.current_division else ""
        )
        self.comboBox_division_list.blockSignals(False)

    def refresh_combobox_department_list(self) -> None:
        self.comboBox_department_list.blockSignals(True)

        self.comboBox_department_list.blockSignals(False)
