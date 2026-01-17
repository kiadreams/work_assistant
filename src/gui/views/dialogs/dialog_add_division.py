from PySide6.QtWidgets import QDialogButtonBox, QWidget

from src.gui.views.dialogs.base_dialog_view import BaseDialogView
from src.gui.views.dialogs.forms.division_form_widget import DivisionFormWidget


class DialogEditView(BaseDialogView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.division_form = DivisionFormWidget(parent=self)

    def initContentWidget(self) -> None:
        super().initContentWidget()
        self.setupConnections()
        self.setWindowTitle("Добавление новой службы")
        self.change_button_box()
        self.verticalLayout.insertWidget(0, self.division_form)

    def setupConnections(self) -> None:
        super().setupConnections()

    def change_button_box(self) -> None:
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Ok)
        if ok_button:
            ok_button.setText("Добавить службу")
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setText("Отмена")
