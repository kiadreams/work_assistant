from dependency_injector import containers, providers

from core.services import employee_service
from gui.models.reports.division_report_table_models import (
    DivisionReportDepartmentTableModel,
    DivisionReportDivisionTableModel,
)
from gui.viewmodels import DivisionViewModel
from gui.views.reports import DivisionReportView


class ReportSessionContainer(containers.DeclarativeContainer):

    # employee_service = providers.Dependency()
    main_container = providers.DependenciesContainer()

    division_viewmodel = providers.Singleton(
        DivisionViewModel,
        employee_service=employee_service,
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
