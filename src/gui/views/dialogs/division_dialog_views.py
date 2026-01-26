from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox, QWidget

from src.core.constants import QtStyleResources
from src.gui.generated.ui.ui_base_dialog_view import Ui_BaseDialogView
from src.gui.utils import ResourceLoader
from src.gui.views.dialogs.forms.dialog_forms import DivisionFormWidget


class BaseDialogView(QDialog, Ui_BaseDialogView):
    data_accepted_signal = Signal(dict)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())

    def setup_connections(self) -> None:
        self.buttonBox_exit.rejected.connect(self.reject)
        self.buttonBox_exit.accepted.connect(self._accepted_data_validate)

    def show_warning_massage(self, text: str) -> None:
        QMessageBox.warning(self, "Ошибка данных", text)

    def _accepted_data_validate(self) -> None:
        self.data_accepted_signal.emit(self.get_data())

    def get_data(self) -> dict[str, str] | None:
        pass


class AddDivisionDialogView(BaseDialogView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._division_form = DivisionFormWidget(parent=self)

    def init_content_widget(self) -> None:
        super().init_content_widget()
        self._division_form.add_division_name_field("Название службы:")
        self._division_form.add_division_full_name_field("Полное наименование службы:")
        self.setup_connections()
        self.setWindowTitle("Добавление новой службы")
        self.change_button_box()
        self.verticalLayout.insertWidget(0, self._division_form)

    def change_button_box(self) -> None:
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Ok)
        if ok_button:
            ok_button.setText("Добавить службу")
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setText("Отмена")

    def get_data(self) -> dict[str, str] | None:
        division_data = self._division_form.get_data()
        return division_data


class EditDivisionDialogView(BaseDialogView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._division_form = DivisionFormWidget(parent=self)

    def init_content_widget(self) -> None:
        super().init_content_widget()
        self._division_form.add_division_name_field("Новое название службы:")
        self._division_form.add_division_full_name_field("Новое полное наименование:")
        self.setup_connections()
        self.setWindowTitle("Изменение данных службы")
        self.change_button_box()
        self.verticalLayout.insertWidget(0, self._division_form)

    def change_button_box(self) -> None:
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Ok)
        if ok_button:
            ok_button.setText("Изменить")
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setText("Отмена")

    def get_data(self) -> dict[str, str] | None:
        division_data = self._division_form.get_data()
        return division_data
