from __future__ import annotations

from typing import TYPE_CHECKING

from src.core.constants import ReportsViews as ViewEnum
from src.core.interfaces.coordinators import ViewCoordinatorProtocol
from src.gui.views.reports_window import ReportsWindow

if TYPE_CHECKING:
    import src.gui.coordinators.reports as reports
    from src.core.interfaces.services import EmployeeServiceProtocol


class ReportsCoordinator:
    def __init__(
        self,
        employee_service: EmployeeServiceProtocol,
        reports_window: ReportsWindow,
        divisions_coordinator: reports.DivisionsCoordinator,
        staff_coordinator: reports.StaffCoordinator,
        work_types_coordinator: reports.WorkTypesCoordinator,
        works_coordinator: reports.WorksCoordinator,
        orders_coordinator: reports.OrdersCoordinator,
        work_events_coordinator: reports.WorkEventsCoordinator,
    ) -> None:
        self.employee_service = employee_service
        self._reports_window = reports_window
        self._view_coordinators: dict[ViewEnum, ViewCoordinatorProtocol] = {
            ViewEnum.DIVISIONS: divisions_coordinator,
            ViewEnum.STAFF: staff_coordinator,
            ViewEnum.WORKS: works_coordinator,
            ViewEnum.ORDERS: orders_coordinator,
            ViewEnum.WORK_EVENTS: work_events_coordinator,
            ViewEnum.WORK_TYPES: work_types_coordinator,
        }

    @property
    def session_window(self) -> ReportsWindow:
        return self._reports_window

    def start(self) -> None:
        self._connect_signals()
        self._initialize_all_views()
        self.open_divisions_view()

    def _initialize_all_views(self) -> None:
        for view_enum, coordinator in self._view_coordinators.items():
            coordinator.start()
            self.session_window.add_view(view_enum, coordinator.view)

    def _connect_signals(self) -> None:
        self.session_window.open_divisions_view_signal.connect(self.open_divisions_view)
        self.session_window.open_staff_view_signal.connect(self.open_staff_view)
        self.session_window.open_works_view_signal.connect(self.open_works_view)
        self.session_window.open_work_events_view_signal.connect(self.open_work_events_view)
        self.session_window.open_work_types_view_signal.connect(self.open_work_types_view)
        self.session_window.open_orders_view_signal.connect(self.open_orders_view)

    def _disconnect_signals(self) -> None:
        self.session_window.open_divisions_view_signal.disconnect(self.open_divisions_view)
        self.session_window.open_staff_view_signal.disconnect(self.open_staff_view)
        self.session_window.open_works_view_signal.disconnect(self.open_works_view)
        self.session_window.open_work_events_view_signal.disconnect(self.open_work_events_view)
        self.session_window.open_work_types_view_signal.disconnect(self.open_work_types_view)
        self.session_window.open_orders_view_signal.disconnect(self.open_orders_view)

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
        self._disconnect_signals()
        for coordinator in self._view_coordinators.values():
            coordinator.teardown()
