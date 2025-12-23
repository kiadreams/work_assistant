from PySide6 import QtWidgets

from scripts.resource_loader import ResourceLoader, get_version_from_file
from ..constants import QtResources


class BaseAppWidgetMixin:
    @property
    def app_version(self) -> str:
        return get_version_from_file()

    def _init_widget_style(self, resources: QtResources) -> None:
        self.setupUi(self)
        self.setStyleSheet(ResourceLoader(resources).load_style())

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
                            exclusive=True) -> QtWidgets.QButtonGroup:
        button_group = QtWidgets.QButtonGroup(self)
        button_group.setExclusive(exclusive)
        for element in elements:
            button, index = element
            button.setCheckable(exclusive)
            button_group.addButton(button, index)
        button_group.setObjectName(name_group)
        return button_group
