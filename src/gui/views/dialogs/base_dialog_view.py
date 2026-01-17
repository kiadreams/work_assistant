from PySide6.QtWidgets import QDialog, QWidget

from src.gui.constants import QtStyleResources
from src.gui.generated.ui.ui_base_dialog_view import Ui_BaseDialogView
from utils.qt_recource_loader import ResourceLoader


class BaseDialogView(QDialog, Ui_BaseDialogView):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def initContentWidget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())

    def setupConnections(self) -> None:
        self.buttonBox_exit.accepted.connect(self.accept)
        self.buttonBox_exit.rejected.connect(self.reject)
