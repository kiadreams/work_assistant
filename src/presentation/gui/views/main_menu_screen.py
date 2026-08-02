from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Qt, Signal, SignalInstance
from PySide6.QtGui import QStandardItemModel

from src.presentation.view_dtos.staff_view_dtos import CompanyViewDto
from src.shared.constants import QtStyleResources

from ..generated import Ui_MainMenuWidget
from .ui_components import BaseView, TypedStandardItem

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class MainMenuScreen(BaseView, Ui_MainMenuWidget):
    to_employees_screen_signal = Signal(CompanyViewDto)
    to_reports_screen_signal = Signal(CompanyViewDto)
    to_protocols_screen_signal = Signal(CompanyViewDto)
    close_app_signal = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._company_model = QStandardItemModel()
        self._init_content_view(QtStyleResources.MAIN_MENU_STYLE)

    def _view_customization(self) -> None:
        self.company_list.setModel(self._company_model)

    def _setup_connections(self) -> None:
        self.exit_btn.clicked.connect(self.close_app_signal.emit)
        self.edit_employee_data_btn.clicked.connect(self._open_employees_view)
        self.create_reports_btn.clicked.connect(self._open_reports_view)
        self.create_protocols_btn.clicked.connect(self._open_protocols_view)

    def set_companies_data(self, companies: list[CompanyViewDto]) -> None:
        self.company_list.blockSignals(True)
        try:
            self._company_model.clear()
            if companies:
                for company in companies:
                    item = TypedStandardItem[CompanyViewDto](company.display_name)
                    item.dto = company
                    self._company_model.appendRow(item)
            else:
                item = TypedStandardItem[None]("В базе данных компаний не найдено")
                item.setFlags(Qt.ItemFlag.ItemIsSelectable)
                self._company_model.appendRow(item)
            self.company_list.setCurrentIndex(0)
        finally:
            self.company_list.blockSignals(False)

    def _open_employees_view(self) -> None:
        self._emit_signal(self.to_employees_screen_signal)

    def _open_reports_view(self) -> None:
        self._emit_signal(self.to_reports_screen_signal)

    def _open_protocols_view(self) -> None:
        self._emit_signal(self.to_protocols_screen_signal)

    def _emit_signal(self, some_signal: SignalInstance) -> CompanyViewDto | None:
        company_index = self.company_list.view().currentIndex()
        company_item = self._company_model.itemFromIndex(company_index)
        if hasattr(company_item, "dto"):
            some_signal.emit(company_item.dto)

