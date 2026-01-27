from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox, QWidget

from src.core.constants import QtStyleResources
from src.gui.dto.gui_dto_models import GuiDivisionDto
from src.gui.generated.ui.ui_base_dialog_view import Ui_BaseDialogView
from src.gui.utils import ResourceLoader
from src.gui.views.dialogs.forms.dialog_forms import StructureFormWidget


class BaseDialogView(QDialog, Ui_BaseDialogView):
    data_accepted_signal = Signal(dict)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._structure_form = StructureFormWidget(parent=self)

    def init_content_view(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.REPORT_WIDGET_STYLE).load_style())
        self.verticalLayout.insertWidget(0, self._structure_form)
        self.setup_connections()

    def setup_connections(self) -> None:
        self.buttonBox_exit.rejected.connect(self.reject)
        self.buttonBox_exit.accepted.connect(self._accepted_data_validate)

    def show_warning_massage(self, title: str, message: str) -> None:
        QMessageBox.warning(self, title, message)

    def _accepted_data_validate(self) -> None:
        self.data_accepted_signal.emit(self.get_data())

    def get_data(self) -> dict[str, str] | None:
        pass

    def set_view_data(self, division_dto: GuiDivisionDto) -> None:
        pass


class AddDivisionDialogView(BaseDialogView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

    def init_content_view(self) -> None:
        super().init_content_view()
        self._structure_form.add_structure_name_field("Название службы:")
        self._structure_form.add_structure_full_name_field("Полное наименование службы:")
        self.setWindowTitle("Добавление новой службы")
        self.change_button_box()

    def change_button_box(self) -> None:
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Ok)
        if ok_button:
            ok_button.setText("Добавить службу")
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setText("Отмена")

    def get_data(self) -> dict[str, str] | None:
        division_data = self._structure_form.get_data()
        return division_data


class EditDivisionDialogView(BaseDialogView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

    def init_content_view(self) -> None:
        super().init_content_view()
        self._structure_form.add_structure_name_field("Новое название службы:")
        self._structure_form.add_structure_full_name_field("Новое полное наименование:")
        self.setWindowTitle("Изменение данных службы")
        self.change_button_box()

    def change_button_box(self) -> None:
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Ok)
        if ok_button:
            ok_button.setText("Изменить")
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setText("Отмена")

    def get_data(self) -> dict[str, str] | None:
        division_data = self._structure_form.get_data()
        return division_data

    def set_view_data(self, division_dto: GuiDivisionDto) -> None:
        self._structure_form.structure_name.setText(division_dto.name)
        self._structure_form.structure_full_name.setText(division_dto.full_name)


class AddDepartmentDialogView(BaseDialogView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

    def init_content_view(self) -> None:
        super().init_content_view()
        self._structure_form.add_structure_name_field("Название отдела:")
        self._structure_form.add_structure_full_name_field("Полное наименование отдела:")
        self.setWindowTitle("Добавление нового отдела")
        self.change_button_box()

    def change_button_box(self) -> None:
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Ok)
        if ok_button:
            ok_button.setText("Добавить отдел")
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setText("Отмена")

    def get_data(self) -> dict[str, str] | None:
        division_data = self._structure_form.get_data()
        return division_data


class EditDepartmentDialogView(BaseDialogView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

    def init_content_view(self) -> None:
        super().init_content_view()
        self._structure_form.add_structure_name_field("Новое название отдела:")
        self._structure_form.add_structure_full_name_field("Новое полное наименование:")
        self.setWindowTitle("Изменение данных отдела")
        self.change_button_box()

    def change_button_box(self) -> None:
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Ok)
        if ok_button:
            ok_button.setText("Изменить")
        ok_button = self.buttonBox_exit.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setText("Отмена")

    def get_data(self) -> dict[str, str] | None:
        division_data = self._structure_form.get_data()
        return division_data

    def set_view_data(self, division_dto: GuiDivisionDto) -> None:
        self._structure_form.structure_name.setText(division_dto.name)
        self._structure_form.structure_full_name.setText(division_dto.full_name)
