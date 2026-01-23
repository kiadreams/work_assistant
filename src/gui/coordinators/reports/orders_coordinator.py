from __future__ import annotations

from typing import TYPE_CHECKING

from src.gui.views.reports import OrderReportView

if TYPE_CHECKING:
    from src.core.interfaces.services import EmployeeServiceProtocol


class OrdersCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol):
        self.employee_service = employee_service
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
