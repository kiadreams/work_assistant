from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Protocol, TypeVar, cast

from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QMessageBox, QWidget

from src.shared.constants import QtStyleResources

from ..generated import ResourceLoader

T = TypeVar("T")


class TypedStandardItem(QStandardItem, Generic[T]):
    dto: T


class BaseView(QWidget):
    if TYPE_CHECKING:

        def setupUi(self, widget: QWidget) -> None: ...  # noqa: N802

    def _init_content_view(self, widget_style: QtStyleResources) -> None:
        self.setupUi(self)
        self.setStyleSheet(ResourceLoader(widget_style).load_style())
        self._view_customization()
        self._setup_connections()

    def _setup_connections(self) -> None:
        pass

    def _view_customization(self) -> None:
        pass

    def show_warning_massage(self, title: str, message: str) -> None:
        QMessageBox.warning(self, title, message)
