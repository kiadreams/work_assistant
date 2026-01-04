from PySide6 import QtWidgets

from src.utils.qt_recource_loader import ResourceLoader
from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_WorkEventReportWidget


class WorkEventReportView(QtWidgets.QWidget, Ui_WorkEventReportWidget):

    def __init__(self) -> None:
        super().__init__()
        self.init_content_view()
        self.__setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())

    def __setup_connections(self) -> None:
        pass
