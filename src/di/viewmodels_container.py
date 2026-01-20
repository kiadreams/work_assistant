from dependency_injector import containers, providers

from di.services_container import ServiceContainer
from gui.models.reports.division_report_table_models import (
    DivisionReportDepartmentTableModel,
    DivisionReportDivisionTableModel,
)
from gui.viewmodels import DivisionViewModel


class ViewModelsContainer(containers.DeclarativeContainer):
    services_container = providers.Container(ServiceContainer)

    division_viewmodel = providers.Factory(
        DivisionViewModel,
        employee_service=services_container.employee_service,
    )
    division_report_division_table_model = providers.Factory(
        DivisionReportDivisionTableModel,
        viewmodel=division_viewmodel,
    )
    division_report_department_table_model = providers.Factory(
        DivisionReportDepartmentTableModel,
        viewmodel=division_viewmodel,
    )
