from PySide6 import QtWidgets

from .base_widgets import BaseAppWidgetMixin
from ..constants import QtStyleResources
from ..windows.ui_work_types_report_widget import Ui_WorkTypeReportsWidget


class WorkTypeReport(QtWidgets.QWidget, Ui_WorkTypeReportsWidget, BaseAppWidgetMixin):

    def __init__(self) -> None:
        super().__init__()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self._init_widget_style(QtStyleResources.REPORT_WIDGET_STYLE)

    def __setup_connections(self) -> None:
        pass
