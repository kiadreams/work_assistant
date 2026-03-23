from __future__ import annotations


from src.core.services import CompanyService
from src.gui.views.reports import OrderReportView


class OrdersCoordinator:
    def __init__(self, company_service: CompanyService):
        self.company_service = company_service
        self._view = OrderReportView()

    def start(self) -> None:
        self._view.init_content_view()
        self._connect_signals()

    @property
    def view(self) -> OrderReportView:
        return self._view

    def _connect_signals(self) -> None:
        pass

    def teardown(self) -> None:
        pass
