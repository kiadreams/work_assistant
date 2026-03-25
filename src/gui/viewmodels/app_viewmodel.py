from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Signal

from src.core.models.company_domain import CompanyDomain
from src.gui.viewmodels.base_view_model import BaseViewModel

if TYPE_CHECKING:
    from src.core.services import CompanyService


class AppViewModel(BaseViewModel):
    company_data_changed_signal = Signal()

    def __init__(
        self,
        company_service: CompanyService,
    ) -> None:
        super().__init__()
        self._company_service = company_service
        self._companies: list[CompanyDomain] = []
        self._current_company: CompanyDomain | None = None

    def init_model_data(self) -> None:
        self.load_all_companies()

    @property
    def companies(self) -> list[CompanyDomain]:
        return self._companies

    @companies.setter
    def companies(self, value: list[CompanyDomain]) -> None:
        self._companies = value
        self.current_company = value[0] if value else None

    @property
    def current_company(self) -> CompanyDomain | None:
        return self._current_company

    @current_company.setter
    def current_company(self, company: CompanyDomain | None) -> None:
        self._current_company = company

    def load_all_companies(self) -> None:
        companies = self._company_service.load_all_divisions()
        self.divisions = divisions