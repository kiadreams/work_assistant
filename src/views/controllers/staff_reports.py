from PySide6 import QtWidgets

from .base_widgets import BaseAppWidgetMixin
from scripts.resource_loader import QtStyleResources
from ..windows.ui_staff_report_widget import Ui_StaffReportsWidget


class StaffReport(QtWidgets.QWidget, Ui_StaffReportsWidget, BaseAppWidgetMixin):

    def __init__(self) -> None:
        super().__init__()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self._init_widget_style(QtStyleResources.REPORT_WIDGET_STYLE)

    def __setup_connections(self) -> None:
        pass
