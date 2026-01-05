from PySide6 import QtWidgets

from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_WorkReportWidget
from src.utils.qt_recource_loader import ResourceLoader


class WorkReportView(QtWidgets.QWidget, Ui_WorkReportWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())

    def __setup_connections(self) -> None:
        pass
