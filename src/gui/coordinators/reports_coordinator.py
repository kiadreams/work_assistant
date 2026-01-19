from __future__ import annotations

from typing import TYPE_CHECKING

import src.gui.coordinators.reports as coordinators
from src.core.constants import ReportsViews as ViewEnum
from src.gui.views.reports_window import ReportsWindow

if TYPE_CHECKING:
    from core.interfaces.coordinators import ViewCoordinatorProtocol
    from core.interfaces.services import EmployeeServiceProtocol


class ReportsCoordinator:
    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        self.employee_service = employee_service
        self._reports_window = ReportsWindow()
        self._view_coordinators: dict[ViewEnum, ViewCoordinatorProtocol] = {}

    @property
    def session_window(self) -> ReportsWindow:
        return self._reports_window

    def start_session(self) -> None:
        self._connect_signals()
        self._initialize_all_views()
        self.open_divisions_view()

    def _initialize_all_views(self) -> None:
        self._view_coordinators[ViewEnum.DIVISIONS] = coordinators.DivisionsCoordinator(
            self.employee_service
        )
        self._view_coordinators[ViewEnum.STAFF] = coordinators.StaffCoordinator(
            self.employee_service
        )
        self._view_coordinators[ViewEnum.WORK_TYPES] = coordinators.WorkTypesCoordinator(
            self.employee_service
        )
        self._view_coordinators[ViewEnum.WORKS] = coordinators.WorksCoordinator(
            self.employee_service
        )
        self._view_coordinators[ViewEnum.ORDERS] = coordinators.OrdersCoordinator(
            self.employee_service
        )
        self._view_coordinators[ViewEnum.WORK_EVENTS] = coordinators.WorkEventsCoordinator(
            self.employee_service
        )

        for view_enum, coordinator in self._view_coordinators.items():
            coordinator.start_view()
            self.session_window.add_view(view_enum, coordinator.view)

    def _connect_signals(self) -> None:
        self.session_window.open_divisions_view_signal.connect(self.open_divisions_view)
        self.session_window.open_staff_view_signal.connect(self.open_staff_view)
        self.session_window.open_works_view_signal.connect(self.open_works_view)
        self.session_window.open_work_events_view_signal.connect(self.open_work_events_view)
        self.session_window.open_work_types_view_signal.connect(self.open_work_types_view)
        self.session_window.open_orders_view_signal.connect(self.open_orders_view)

    def open_divisions_view(self) -> None:
        self.session_window.change_view(ViewEnum.DIVISIONS)

    def open_staff_view(self) -> None:
        self.session_window.change_view(ViewEnum.STAFF)

    def open_work_types_view(self) -> None:
        self.session_window.change_view(ViewEnum.WORK_TYPES)

    def open_works_view(self) -> None:
        self.session_window.change_view(ViewEnum.WORKS)

    def open_orders_view(self) -> None:
        self.session_window.change_view(ViewEnum.ORDERS)

    def open_work_events_view(self) -> None:
        self.session_window.change_view(ViewEnum.WORK_EVENTS)

    def teardown(self) -> None:
        """Очистка всех внутренних ресурсов сессии."""
        for coordinator in self._view_coordinators.values():
            if hasattr(coordinator, "teardown"):
                coordinator.teardown()
