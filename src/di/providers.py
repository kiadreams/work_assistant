from dishka import Container, Provider, Scope, provide
from sqlalchemy.orm import Session

from src.core.interfaces.coordinators import (
    AppCoordinatorProtocol,
    ProtocolsCoordinatorProtocol,
    ReportsCoordinatorProtocol,
)
from src.core.interfaces.factories import AppFactoryProtocol
from src.core.interfaces.invokers import OperationInvokerProtocol
from src.core.interfaces.repositories import DatabaseManagerProtocol, DivisionRepositoryProtocol
from src.core.interfaces.services import EmployeeServiceProtocol
from src.core.interfaces.ui import (
    MainMenuViewProtocol,
    MainWindowViewProtocol,
    ReportsWindowViewProtocol,
)
from src.core.interfaces.viewmodels import DivisionViewModelProtocol
from src.database.db_manager import DatabaseManager
from src.database.repositories.division_repository import DivisionRepository
from src.di.factories import AppFactory
from src.di.invokers import OperationInvoker
from src.gui.coordinators import (
    AppCoordinator,
    ProtocolsCoordinator,
    ReportsCoordinator,
)
from src.gui.views import (
    DivisionReportView,
    MainMenuView,
    MainWindowView,
    OrderReportView,
    ReportsWindowView,
    StaffReportView,
    WorkEventReportView,
    WorkReportView,
    WorkTypeReportView,
)
from src.services.EmployeeService import EmployeeService
from src.viewmodels import DivisionViewModel
from src.viewmodels.qt_interfaces import QtDivisionVMProtocol


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def db_manager(self) -> DatabaseManagerProtocol:
        return DatabaseManager()

    @provide(scope=Scope.REQUEST)
    def db_session(self, manager: DatabaseManagerProtocol) -> Session:
        return manager.create_session()

    @provide(scope=Scope.REQUEST)
    def division_repository(self, curr_session: Session) -> DivisionRepositoryProtocol:
        return DivisionRepository(session=curr_session)


class FactoriesProvider(Provider):
    @provide(scope=Scope.APP)
    def operation_invoker(self, root_container: Container) -> OperationInvokerProtocol:
        return OperationInvoker(root_container=root_container)

    @provide(scope=Scope.APP)
    def app_factory(self, root_container: Container) -> AppFactoryProtocol:
        return AppFactory(root_container=root_container)


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def employee_service(
        self, divisions_repository: DivisionRepositoryProtocol
    ) -> EmployeeServiceProtocol:
        return EmployeeService(division_repository=divisions_repository)


class ViewmodelProvider(Provider):
    @provide(scope=Scope.APP)
    def division_viewmodel(
        self,
        operation_invokers: OperationInvokerProtocol,
    ) -> QtDivisionVMProtocol:
        return DivisionViewModel(operation_invoker=operation_invokers)


class UIWindowsProvider(Provider):
    @provide(scope=Scope.APP)
    def main_window(self) -> MainWindowViewProtocol:
        return MainWindowView()

    @provide(scope=Scope.APP)
    def main_menu_ui(self) -> MainMenuViewProtocol:
        return MainMenuView()

    @provide(scope=Scope.APP)
    def reports_window_ui(self) -> ReportsWindowViewProtocol:
        return ReportsWindowView()

    @provide(scope=Scope.SESSION)
    def division_report_ui(self, viewmodel: QtDivisionVMProtocol) -> DivisionReportView:
        return DivisionReportView(viewmodel=viewmodel)

    @provide(scope=Scope.SESSION)
    def order_report_ui(self) -> OrderReportView:
        return OrderReportView()

    @provide(scope=Scope.SESSION)
    def staff_report_ui(self) -> StaffReportView:
        return StaffReportView()

    @provide(scope=Scope.SESSION)
    def work_event_report_ui(self) -> WorkEventReportView:
        return WorkEventReportView()

    @provide(scope=Scope.SESSION)
    def work_report_ui(self) -> WorkReportView:
        return WorkReportView()

    @provide(scope=Scope.SESSION)
    def work_type_report_ui(self) -> WorkTypeReportView:
        return WorkTypeReportView()


class CoordinatorsProvider(Provider):
    @provide(scope=Scope.APP)
    def app_coordinator(
        self,
        window_factory: AppFactoryProtocol,
    ) -> AppCoordinatorProtocol:
        return AppCoordinator(window_factory=window_factory)

    @provide(scope=Scope.SESSION)
    def reports_coordinator(
        self,
        reports_window: ReportsWindowViewProtocol,
        container: Container,
    ) -> ReportsCoordinatorProtocol:
        return ReportsCoordinator(reports_window, container)

    @provide(scope=Scope.SESSION)
    def protocols_coordinator(
        self,
    ) -> ProtocolsCoordinatorProtocol:
        return ProtocolsCoordinator()
