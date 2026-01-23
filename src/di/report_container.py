from __future__ import annotations

from typing import TYPE_CHECKING

from dependency_injector import containers, providers

from src.core.validators.division_validator import DivisionValidator
from src.gui.coordinators.reports import (
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
    from src.core.services import EmployeeService


class ReportSessionContainer(containers.DeclarativeContainer):
    employee_service: providers.Dependency[EmployeeService] = providers.Dependency()
    division_validator: providers.Dependency[DivisionValidator] = providers.Dependency()

    division_viewmodel = providers.Singleton(
        DivisionViewModel,
        employee_service=employee_service,
        division_validator=division_validator,
    )

    division_report_division_table_model = providers.Singleton(
        DivisionReportDivisionTableModel,
        viewmodel=division_viewmodel,
    )
    division_report_department_table_model = providers.Singleton(
        DivisionReportDepartmentTableModel,
        viewmodel=division_viewmodel,
    )

    division_report_view = providers.Singleton(
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
        employee_service=employee_service,
    )
    staff_coordinator = providers.Singleton(
        StaffCoordinator,
        employee_service=employee_service,
    )
    work_events_coordinator = providers.Singleton(
        WorkEventsCoordinator,
        employee_service=employee_service,
    )
    works_types_coordinator = providers.Singleton(
        WorkTypesCoordinator,
        employee_service=employee_service,
    )
    works_coordinator = providers.Singleton(
        WorksCoordinator,
        employee_service=employee_service,
    )

    reports_window = providers.Singleton(ReportsWindow)

    reports_coordinator = providers.Singleton(
        ReportsCoordinator,
        report_window=reports_window,
        employee_service=employee_service,
        divisions_coordinator=division_coordinator,
        staff_coordinator=staff_coordinator,
        work_types_coordinator=works_types_coordinator,
        works_coordinator=works_coordinator,
        orders_coordinator=orders_coordinator,
        work_events_coordinator=work_events_coordinator,
    )
