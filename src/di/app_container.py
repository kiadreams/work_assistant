from dependency_injector import containers, providers

from core.services import EmployeeService
from core.validators.division_validator import DivisionValidator
from di.report_session_container import ReportSessionContainer
from gui.views import MainMenuWindow, MainWindow
from infrastucture.database import DatabaseManager
from infrastucture.database.repositories import DivisionRepository


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()



    db_manager = providers.Singleton(DatabaseManager)

    division_repository = providers.Singleton(DivisionRepository, db_manager=db_manager)

    employee_service = providers.Singleton(EmployeeService, division_repository=division_repository)
    division_validator = providers.Singleton(DivisionValidator, employee_service=employee_service)

    main_window = providers.Singleton(MainWindow)
    main_menu_window = providers.Singleton(MainMenuWindow)

    report_session_factory = providers.Factory(
        ReportSessionContainer,
    )
