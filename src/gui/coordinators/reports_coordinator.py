from __future__ import annotations

from typing import TYPE_CHECKING

import src.gui.coordinators.reports as coordinators
from src.core.constants import PageStructure
from src.core.constants import ReportsViews as ViewEnum
from src.gui.views.reports_window import ReportsWindow

if TYPE_CHECKING:
    from core.interfaces.coordinators import ViewCoordinatorProtocol
    from core.interfaces.services import EmployeeServiceProtocol


class ReportsCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service
        self._reports_window = ReportsWindow()
        self._view_coordinator: ViewCoordinatorProtocol | None = None

    @property
    def session_window(self) -> ReportsWindow:
        return self._reports_window

    def start_session(self) -> None:
        self._connect_signals()
        self.open_divisions_view()

    def _connect_signals(self) -> None:
        self.session_window.open_divisions_view_signal.connect(self.open_divisions_view)
        self.session_window.open_staff_view_signal.connect(self.open_staff_view)
        self.session_window.open_works_view_signal.connect(self.open_works_view)
        self.session_window.open_work_events_view_signal.connect(self.open_work_events_view)
        self.session_window.open_work_types_view_signal.connect(self.open_work_types_view)
        self.session_window.open_orders_view_signal.connect(self.open_orders_view)

    def open_divisions_view(self) -> None:
        self._view_coordinator = coordinators.DivisionsCoordinator(self.employee_service)
        self._open_view(ViewEnum.DIVISIONS)

    def open_staff_view(self) -> None:
        self._view_coordinator = coordinators.StaffCoordinator(self.employee_service)
        self._open_view(ViewEnum.STAFF)

    def open_work_types_view(self) -> None:
        self._view_coordinator = coordinators.WorkTypesCoordinator(self.employee_service)
        self._open_view(ViewEnum.WORK_TYPES)

    def open_works_view(self) -> None:
        self._view_coordinator = coordinators.WorksCoordinator(self.employee_service)
        self._open_view(ViewEnum.WORKS)

    def open_orders_view(self) -> None:
        self._view_coordinator = coordinators.OrdersCoordinator(self.employee_service)
        self._open_view(ViewEnum.ORDERS)

    def open_work_events_view(self) -> None:
        self._view_coordinator = coordinators.WorkEventsCoordinator(self.employee_service)
        self._open_view(ViewEnum.WORK_EVENTS)

    def _open_view(self, view: PageStructure) -> None:
        if self._view_coordinator:
            self._view_coordinator.start_view()
            self.session_window.add_view(view, self._view_coordinator.view)
            self.session_window.change_view(view)
