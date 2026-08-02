from src.presentation.gui.generated import ResourceLoader, Ui_WorkTypeReportWidget
from src.presentation.gui.views.ui_components import BaseView
from src.shared.constants import QtStyleResources


class WorkTypeReportWidget(BaseView, Ui_WorkTypeReportWidget):
    def __init__(self) -> None:
        super().__init__()

    def _init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self._setup_connections()

    def _setup_connections(self) -> None:
        pass
