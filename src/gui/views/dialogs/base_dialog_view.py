from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QWidget

from src.core.constants import QtStyleResources
from src.gui.generated.ui.ui_base_dialog_view import Ui_BaseDialogView
from src.gui.utils import ResourceLoader


class BaseDialogView(QDialog, Ui_BaseDialogView):
    data_accepted_signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())

    def setup_connections(self) -> None:
        self.buttonBox_exit.rejected.connect(self.reject)
        self.buttonBox_exit.accepted.connect(self.data_accepted_signal.emit)

    def get_data(self) -> dict[str, str] | None:
        pass
