from __future__ import annotations

from typing import TYPE_CHECKING

from dependency_injector import containers, providers

from core.validators.division_validator import DivisionValidator
from gui.coordinators.reports import (
    DivisionsCoordinator,
    OrdersCoordinator,
    StaffCoordinator,
    WorkEventsCoordinator,
    WorksCoordinator,
    WorkTypesCoordinator,
)
from src.gui.coordinators.reports_coordinator import ReportsCoordinator
from src.gui.models.reports.division_report_table_models import (
    DivisionReportDepartmentTableModel,
    DivisionReportDivisionTableModel,
)
from src.gui.viewmodels import DivisionViewModel
from src.gui.views import ReportsWindow
from src.gui.views.reports import DivisionReportView

if TYPE_CHECKING:
    from core.services import EmployeeService


class ReportSessionContainer(containers.DeclarativeContainer):
    employee_service: providers.Dependency[EmployeeService] = providers.Dependency()
    division_validator: providers.Dependency[DivisionValidator] = providers.Dependency()

    division_viewmodel = providers.Factory(
        DivisionViewModel,
        employee_service=employee_service,
        division_validator=division_validator,
    )

    division_report_division_table_model = providers.Factory(
        DivisionReportDivisionTableModel,
        viewmodel=division_viewmodel,
    )
    division_report_department_table_model = providers.Factory(
        DivisionReportDepartmentTableModel,
        viewmodel=division_viewmodel,
    )

    division_report_view = providers.Factory(
        DivisionReportView,
        division_table_model=division_report_division_table_model,
        department_table_model=division_report_department_table_model,
    )

    division_coordinator = providers.Singleton(
        DivisionsCoordinator,
        division_viewmodel=division_viewmodel,
        division_report_view=division_report_view,
    )
    orders_coordinator = providers.Singleton(
        OrdersCoordinator,
    )
    staff_coordinator = providers.Singleton(
        StaffCoordinator,
    )
    work_events_coordinator = providers.Singleton(
        WorkEventsCoordinator,
    )
    works_types_coordinator = providers.Singleton(
        WorkTypesCoordinator,
    )
    work_coordinator = providers.Singleton(
        WorksCoordinator,
    )

    reports_window = providers.Factory(ReportsWindow)

    reports_coordinator = providers.Factory(
        ReportsCoordinator,
        reports_window=reports_window,
        employee_service=employee_service,
    )
