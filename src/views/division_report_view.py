from typing import Callable

from PySide6 import QtWidgets

from ..utils.qt_recource_loader import ResourceLoader
from .dialog_edit_view import DialogEditView
from src.constants import QtStyleResources
from src.views.generated.ui.ui_divisions_report_widget import Ui_DivisionReportWidget
from src.view_models.division_viewmodel import DivisionViewModel


class DivisionReportView(QtWidgets.QWidget, Ui_DivisionReportWidget):

    def __init__(self, viewmodel: DivisionViewModel) -> None:
        super().__init__()
        self.model = viewmodel
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.refresh_division_report()

    def __setup_connections(self) -> None:
        self.pushButton_add_division.clicked.connect(self.push_add_division)
        self.pushButton_remove_division.clicked.connect(self.push_remove_division)
        self.pushButton_edit_division.clicked.connect(self.push_edit_division)
        self.pushButton_add_department.clicked.connect(self.push_add_department)
        self.pushButton_remove_department.clicked.connect(self.push_remove_department)
        self.pushButton_edit_department.clicked.connect(self.push_edit_department)
        self.comboBox_division_list.currentTextChanged.connect(self.change_current_division)

    def change_current_division(self, service_name: str) -> None:
        self.model.change_current_division(service_name)
        self.refresh_division_report()

    def refresh_division_report(self) -> None:
        self.refresh_combobox_division_list()
        self.check_enabled_division_deleted_button()

    def check_enabled_division_deleted_button(self) -> None:
        is_enabled = self.model.can_delete_current_division()
        self.pushButton_remove_division.setEnabled(is_enabled)

    def push_add_division(self) -> None:
        self.call_data_dialog()

    def push_remove_division(self) -> None:
        if self.model.can_delete_current_division():
            self.ask_for_confirmation(
                f"Вы уверены, что хотите безвозвратно удалить службу {self.model.current_service}? "
                "Отменить это действие будет невозможно...",
                self.delete_current_division,
            )

    def push_edit_division(self) -> None:
        self.call_data_dialog()

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
        self.model.delete_current_division()
        self.refresh_division_report()

    def refresh_combobox_division_list(self) -> None:
        self.comboBox_division_list.blockSignals(True)
        self.comboBox_division_list.clear()
        self.comboBox_division_list.addItems(self.model.services)
        self.comboBox_division_list.setCurrentText(self.model.current_service)
        self.comboBox_division_list.blockSignals(False)

    def refresh_combobox_department_list(self) -> None:
        self.comboBox_department_list.blockSignals(True)

        self.comboBox_department_list.blockSignals(False)
