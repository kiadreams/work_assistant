from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Signal

from src.shared.constants import QtStyleResources

from ..generated import ResourceLoader, Ui_EmployeesWidget
from .base_view import BaseView

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class EmployeesScreen(BaseView, Ui_EmployeesWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_content_view()
        self.setup_connections()

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.setup_connections()

    def setup_connections(self) -> None:
        pass
