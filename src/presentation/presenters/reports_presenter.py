from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from src.coordinators.main_window_coordinator import MainWindowCoordinator
from src.core.interfaces.coordinators import ViewCoordinatorProtocol
from src.gui.viewmodels import CompanyViewModel
from src.gui.views.reports_widget import ReportsWidget
from src.presentation.presenters.base_presenters.base_presenter import BasePresenter
from src.shared.constants import ReportsViews as ViewEnum

if TYPE_CHECKING:
    import reports
    from


class ReportWidgets(StrEnum):
    DIVISIONS = "divisions_widget"
    EMPLOYEES = "employees_widget"
    WORKS = "works_widget"
    ORDERS = "orders_widget"
    WORK_EVENTS = "work_events_widget"
    WORK_TYPES = "work_types_widget"


class ReportsPresenter(BasePresenter):
    def __init__(
        self,
        company_viewmodel: CompanyViewModel,
        reports_window: ReportsWidget,
        divisions_coordinator: reports.DivisionReportPresenter,
        staff_coordinator: reports.StaffReportPresenter,
        work_types_coordinator: reports.WorkTypeReportPresenter,
        works_coordinator: reports.WorkReportPresenter,
        orders_coordinator: reports.OrderReportPresenter,
        work_events_coordinator: reports.WorkEventReportPresenter,
        coordinator: MainWindowCoordinator,
        widget_index: int,
    ) -> None:
        super().__init__(coordinator, widget_index)
        self._company_viewmodel = company_viewmodel
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
    def session_window(self) -> ReportsWidget:
        return self._reports_window

    @property
    def company_model(self) -> CompanyViewModel:
        return self._company_viewmodel

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
