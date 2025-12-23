from typing import Callable

from PySide6 import QtWidgets

from .base_widgets import BaseAppWidgetMixin, ViewServiceModel
from .dialog_edit_data import DialogEditData
from scripts.resource_loader import QtStyleResources
from ..windows.ui_services_report_widget import Ui_ServiceReportsWidget


class ServiceReport(QtWidgets.QWidget, Ui_ServiceReportsWidget, BaseAppWidgetMixin):

    def __init__(self, view_model: ViewServiceModel) -> None:
        super().__init__()
        self.model = view_model
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self._init_widget_style(QtStyleResources.REPORT_WIDGET_STYLE)
        self.refresh_service_report()

    def __setup_connections(self) -> None:
        self.pushButton_add_service.clicked.connect(self.push_add_service)
        self.pushButton_remove_service.clicked.connect(self.push_remove_service)
        self.pushButton_edit_service.clicked.connect(self.push_edit_service)
        self.pushButton_add_group.clicked.connect(self.push_add_group)
        self.pushButton_remove_group.clicked.connect(self.push_remove_group)
        self.pushButton_edit_group.clicked.connect(self.push_edit_group)
        self.comboBox_service_list.currentTextChanged.connect(self.change_current_service)

    def change_current_service(self, service_name: str) -> None:
        self.model.change_current_service(service_name)
        self.refresh_service_report()

    def refresh_service_report(self):
        self.refresh_combobox_service_list()
        self.check_enabled_service_deleted_button()

    def check_enabled_service_deleted_button(self) -> None:
        is_enabled = self.model.can_delete_current_service()
        self.pushButton_remove_service.setEnabled(is_enabled)

    def push_add_service(self) -> None:
        self.call_data_dialog()

    def push_remove_service(self) -> None:
        if self.model.can_delete_current_service():
            self.ask_for_confirmation(
                f'Вы уверены, что хотите безвозвратно удалить службу {self.model.current_service}? '
                'Отменить это действие будет невозможно...',
                self.delete_current_service
            )

    def push_edit_service(self) -> None:
        self.call_data_dialog()

    def push_add_group(self) -> None:
        self.call_data_dialog()

    def push_remove_group(self) -> None:
        self.call_data_dialog()

    def push_edit_group(self) -> None:
        self.call_data_dialog()

    def call_data_dialog(self) -> None:
        dialog = DialogEditData(self)
        result = dialog.exec_()
        if result == DialogEditData.DialogCode.Accepted:
            pass
        else:
            pass

    def ask_for_confirmation(self, message_text: str, action: Callable[[], None]) -> None:
        reply = QtWidgets.QMessageBox.question(
            self,  # Родительский виджет (наше главное окно)
            'Подтверждение действия',  # Заголовок окна (Title bar)
            message_text,  # Текст сообщения
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,  # Комбинация стандартных кнопок
            QtWidgets.QMessageBox.StandardButton.No  # Кнопка по умолчанию (выделенная)
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Пользователь подтвердил действие. Выполняем удаление...")
            action()

    def delete_current_service(self) -> None:
        self.model.delete_current_service()
        self.refresh_service_report()

    def refresh_combobox_service_list(self) -> None:
        self.comboBox_service_list.blockSignals(True)
        self.comboBox_service_list.clear()
        self.comboBox_service_list.addItems(self.model.services)
        self.comboBox_service_list.setCurrentText(self.model.current_service)
        self.comboBox_service_list.blockSignals(False)

    def refresh_combobox_group_list(self) -> None:
        self.comboBox_group_list.blockSignals(True)

        self.comboBox_group_list.blockSignals(False)
