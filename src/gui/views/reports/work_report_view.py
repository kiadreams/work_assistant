from core.constants import QtStyleResources
from src.gui.generated import Ui_WorkReportWidget
from src.gui.views.base_views import BaseView
from src.utils.qt_recource_loader import ResourceLoader


class WorkReportView(BaseView, Ui_WorkReportWidget):
    def __init__(self) -> None:
        super().__init__()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.__setup_connections()

    def __setup_connections(self) -> None:
        pass
