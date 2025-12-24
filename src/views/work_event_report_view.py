from PySide6 import QtWidgets

from ..utils.qt_recource_loader import ResourceLoader
from src.constants import QtStyleResources
from src.views.generated.ui.ui_work_events_report_widget import Ui_WorkEventReportWidget


class WorkEventReportView(QtWidgets.QWidget, Ui_WorkEventReportWidget):

    def __init__(self) -> None:
        super().__init__()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())

    def __setup_connections(self) -> None:
        pass
