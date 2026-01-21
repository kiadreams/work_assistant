from dependency_injector import containers, providers

from di.viewmodels_container import ViewModelsContainer
from gui.views import AddDivisionDialogView
from gui.views.reports import (
    OrderReportView,
    StaffReportView,
    WorkEventReportView,
    WorkReportView,
    WorkTypeReportView,
)


class ViewsContainer(containers.DeclarativeContainer):
    view_models_container = providers.Container(ViewModelsContainer)


    order_report_view = providers.Factory(OrderReportView)
    staff_report_view = providers.Factory(StaffReportView)
    work_event_report_view = providers.Factory(WorkEventReportView)
    work_report_view = providers.Factory(WorkReportView)
    work_type_report_view = providers.Factory(WorkTypeReportView)
    add_division_dialog_view = providers.Factory(AddDivisionDialogView, parent=providers.Required)
