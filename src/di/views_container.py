from dependency_injector import containers, providers

from di.viewmodels_container import ViewModelsContainer
from gui.views import MainMenuWindow, MainWindow, AddDivisionDialogView
from gui.views.reports import (
    DivisionReportView,
    OrderReportView,
    StaffReportView,
    WorkEventReportView,
    WorkReportView,
    WorkTypeReportView,
)


class ViewsContainer(containers.DeclarativeContainer):

    view_models_container = providers.Container(ViewModelsContainer)

    main_window = providers.Singleton(MainWindow)
    main_menu_window = providers.Singleton(MainMenuWindow)
    division_report_view = providers.Factory(
        DivisionReportView,
        division_table_model=view_models_container.division_report_division_table_model,
        department_table_model=view_models_container.division_report_department_table_model,
    )
    order_report_view = providers.Factory(OrderReportView)
    staff_report_view = providers.Factory(StaffReportView)
    work_event_report_view = providers.Factory(WorkEventReportView)
    work_report_view = providers.Factory(WorkReportView)
    work_type_report_view = providers.Factory(WorkTypeReportView)
    add_division_dialog_view = providers.Factory(AddDivisionDialogView, parent=providers.Required)
