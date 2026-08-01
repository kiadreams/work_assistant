from __future__ import annotations

from src.domain.services import EmployeeService
from src.gui.views.reports import OrderReportWidget


class OrderReportPresenter:
    def __init__(self, company_service: EmployeeService):
        self.company_service = company_service
        self._view = OrderReportWidget()

    def start(self) -> None:
        self._view._init_content_view()
        self._connect_signals()

    @property
    def view(self) -> OrderReportWidget:
        return self._view

    def _connect_signals(self) -> None:
        pass

    def teardown(self) -> None:
        pass
