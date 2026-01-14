from PySide6.QtWidgets import QDialog

from src.gui.constants import QtStyleResources
from src.gui.generated.ui.ui_base_dialog_view import Ui_BaseDialogView


class BaseDialogView(QDialog, Ui_BaseDialogView):
    def __init__(self, parent: None = None) -> None:
        super().__init__(parent)
        self.init_content_widget()
        self.__setup_connections()

    def init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(QtStyleResources.REPORT_WIDGET_STYLE)

    def __setup_connections(self) -> None:
        pass
