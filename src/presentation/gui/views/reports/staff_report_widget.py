from src.gui.generated import Ui_StaffReportWidget
from src.gui.utils import ResourceLoader
from src.gui.views.base_widget import BaseWidget
from src.shared.constants import QtStyleResources


class StaffReportWidget(BaseWidget, Ui_StaffReportWidget):
    def __init__(self) -> None:
        super().__init__()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.setup_connections()

    def setup_connections(self) -> None:
        pass
