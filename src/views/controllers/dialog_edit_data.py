from PySide6 import QtWidgets

# from .base_widgets import BaseAppWidgetMixin
# from ..resource_loader import QtStyleResources
from ..windows.ui_edit_data_dialog import Ui_DialogEditData


class DialogEditData(QtWidgets.QDialog, Ui_DialogEditData):

    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super().__init__(parent)
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        pass
        # self.setupUi(self)
        # self._init_widget_style(QtStyleResources.REPORT_WIDGET_STYLE)

    def __setup_connections(self) -> None:
        pass
