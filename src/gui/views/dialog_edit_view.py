from PySide6 import QtWidgets

from src.gui.generated import Ui_DialogEditData


class DialogEditView(QtWidgets.QDialog, Ui_DialogEditData):
    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super().__init__(parent)
        self.init_content_widget()
        self.__setup_connections()

    def init_content_widget(self) -> None:
        self.setupUi(self)
        # self._init_widget_style(QtStyleResources.REPORT_WIDGET_STYLE)

    def __setup_connections(self) -> None:
        pass
