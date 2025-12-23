from typing import Self

from PySide6 import QtWidgets

from src.utils.qt_recource_loader import ResourceLoader
from src.utils.version import get_version_from_file
from ..constants import QtResources
from src.interfaces.base_widgets import IBaseAppWidget


class BaseAppWidgetMixin:
    @property
    def app_version(self) -> str:
        return get_version_from_file()

    def _init_widget_style(self: IBaseAppWidget | Self, resources: QtResources) -> None:  # type: ignore[misc]
        self.setupUi()  # type: ignore[union-attr]
        self.setStyleSheet(ResourceLoader(resources).load_style())  # type: ignore[union-attr]

    @staticmethod
    def get_widget_to_insert(widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        widget.setLayout(layout)
        return widget


class BaseButtonGroupMixin:
    def create_button_group(self,
                            name_group: str,
                            elements: list[tuple[QtWidgets.QPushButton, int]],
                            exclusive: bool =True) -> QtWidgets.QButtonGroup:
        button_group = QtWidgets.QButtonGroup()
        button_group.setExclusive(exclusive)
        for element in elements:
            button, index = element
            button.setCheckable(exclusive)
            button_group.addButton(button, index)
        button_group.setObjectName(name_group)
        return button_group
