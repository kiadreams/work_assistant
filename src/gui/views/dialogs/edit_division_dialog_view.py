from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtWidgets import QDialogButtonBox, QWidget

from src.gui.views.dialogs.base_dialog_view import BaseDialogView
from src.gui.views.dialogs.forms.dialog_forms import DivisionFormWidget

if TYPE_CHECKING:
    from src.core.interfaces.dto_protocols import DivisionDtoProtocol


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
