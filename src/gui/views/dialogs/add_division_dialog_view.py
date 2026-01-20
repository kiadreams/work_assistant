from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtWidgets import QDialogButtonBox, QWidget

from src.gui.views.dialogs.base_dialog_view import BaseDialogView
from src.gui.views.dialogs.forms.dialog_forms import DivisionFormWidget

if TYPE_CHECKING:
    from src.core.interfaces.data_protocols import DivisionDataProtocol


class AddDivisionDialogView(BaseDialogView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self.new_division_dto: DivisionDataProtocol | None = None
        self._division_form = DivisionFormWidget(parent=self)

    def init_content_widget(self) -> None:
        super().init_content_widget()
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
