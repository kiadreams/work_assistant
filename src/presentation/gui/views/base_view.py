from __future__ import annotations

from PySide6.QtWidgets import QMessageBox, QWidget

from src.shared.constants import QtStyleResources

from ..generated import ResourceLoader


class BaseView(QWidget):
    def _init_content_view(self, widget_style: QtStyleResources) -> None:
        self.setupUi(self)  # noqa: PyUnresolvedReferences, N802
        self.setStyleSheet(ResourceLoader(widget_style).load_style())
        self._view_customization()
        self._setup_connections()

    def _setup_connections(self) -> None:
        pass

    def _view_customization(self) -> None:
        pass

    def show_warning_massage(self, title: str, message: str) -> None:
        QMessageBox.warning(self, title, message)
