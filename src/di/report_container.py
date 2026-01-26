from __future__ import annotations

from typing import TYPE_CHECKING

from dependency_injector import containers, providers

import src.gui.coordinators.reports as report_coordinators
from src.core.validators.division_validators import DepartmentValidator, DivisionValidator
from src.gui.coordinators.reports_coordinator import ReportsCoordinator
from src.gui.dto.model_pipeline_services import DepartmentPipelineService, DivisionPipelineService
from src.gui.models.reports.division_report_table_models import (
    DivisionReportDepartmentTableModel,
    DivisionReportDivisionTableModel,
)
from src.gui.viewmodels import DivisionViewModel
from src.gui.viewmodels.dialogs.division_dialog_models import (
    AddDepartmentDialogModel,
    AddDivisionDialogModel,
    EditDepartmentDialogModel,
    EditDivisionDialogModel,
)
from src.gui.views import ReportsWindow
from src.gui.views.dialogs.division_dialog_views import (
    AddDepartmentDialogView,
    AddDivisionDialogView,
    EditDepartmentDialogView,
    EditDivisionDialogView,
)
from src.gui.views.reports import DivisionReportView
from src.shared.mappers.mapper_services import DepartmentMapperService, DivisionMapperService

if TYPE_CHECKING:
    from src.core.services import EmployeeService


class DivisionDialogContainer(containers.DeclarativeContainer):
    employee_service: providers.Dependency[EmployeeService] = providers.Dependency()
    reports_window: providers.Dependency[ReportsWindow] = providers.Dependency()
    division_viewmodel: providers.Dependency[DivisionViewModel] = providers.Dependency()

    division_validator = providers.Factory(DivisionValidator, employee_service=employee_service)
    division_mapper_service = providers.Factory(DivisionMapperService)

    department_validator = providers.Factory(DepartmentValidator, employee_service=employee_service)
    department_mapper_service = providers.Factory(DepartmentMapperService)

    division_pipeline_service = providers.Factory(
        DivisionPipelineService,
        division_validator=division_validator,
    )
    department_pipeline_service = providers.Factory(
        DepartmentPipelineService,
        department_validator=department_validator,
    )

    add_division_dialog_model = providers.Factory(
        AddDivisionDialogModel, division_pipeline_service=division_pipeline_service
    )
    edit_division_dialog_model = providers.Factory(
        EditDivisionDialogModel,
        division_pipeline_service=division_pipeline_service,
        division_mapper_service=division_mapper_service,
        current_division=providers.AttributeGetter(division_viewmodel, "current_division"),
    )
    add_department_dialog_model = providers.Factory(
        AddDepartmentDialogModel, department_pipeline_service=department_pipeline_service
    )
    edit_department_dialog_model = providers.Factory(
        EditDepartmentDialogModel,
        department_pipeline_service=department_pipeline_service,
        department_mapper_service=department_mapper_service,
        current_department=providers.AttributeGetter(division_viewmodel, "current_department"),
    )

    add_division_dialog_view = providers.Factory(AddDivisionDialogView, parent=reports_window)
    edit_division_dialog_view = providers.Factory(EditDivisionDialogView, parent=reports_window)
    add_department_dialog_view = providers.Factory(AddDepartmentDialogView, parent=reports_window)
    edit_department_dialog_view = providers.Factory(EditDepartmentDialogView, parent=reports_window)


class ReportSessionContainer(containers.DeclarativeContainer):
    employee_service: providers.Dependency[EmployeeService] = providers.Dependency()

    reports_window = providers.Singleton(ReportsWindow)
    division_viewmodel = providers.Singleton(DivisionViewModel, employee_service=employee_service)

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

    orders_coordinator = providers.Singleton(
        report_coordinators.OrdersCoordinator,
        employee_service=employee_service,
    )
    staff_coordinator = providers.Singleton(
        report_coordinators.StaffCoordinator,
        employee_service=employee_service,
    )
    work_events_coordinator = providers.Singleton(
        report_coordinators.WorkEventsCoordinator,
        employee_service=employee_service,
    )
    works_types_coordinator = providers.Singleton(
        report_coordinators.WorkTypesCoordinator,
        employee_service=employee_service,
    )
    works_coordinator = providers.Singleton(
        report_coordinators.WorksCoordinator,
        employee_service=employee_service,
    )
    division_dialog_container = providers.Factory(
        DivisionDialogContainer,
        employee_service=employee_service,
        reports_window=reports_window,
        division_viewmodel=division_viewmodel,
    )

    division_coordinator = providers.Singleton(
        report_coordinators.DivisionsCoordinator,
        division_viewmodel=division_viewmodel,
        division_report_view=division_report_view,
        division_dialog_factory=division_dialog_container.provider,
    )

    reports_coordinator = providers.Singleton(
        ReportsCoordinator,
        reports_window=reports_window,
        employee_service=employee_service,
        divisions_coordinator=division_coordinator,
        staff_coordinator=staff_coordinator,
        work_types_coordinator=works_types_coordinator,
        works_coordinator=works_coordinator,
        orders_coordinator=orders_coordinator,
        work_events_coordinator=work_events_coordinator,
    )
