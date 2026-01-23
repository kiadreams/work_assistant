from __future__ import annotations

from dependency_injector import containers, providers

from core.validators.division_validator import DivisionValidator
from di.report_container import ReportSessionContainer
from gui.views import MainMenuWindow, MainWindow
from infrastucture.database import DatabaseManager
from infrastucture.database.repositories import DivisionRepository
from src.core.services import EmployeeService
from src.gui.coordinators.app_coordinator import AppCoordinator


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_manager = providers.Singleton(DatabaseManager)

    division_repository = providers.Singleton(DivisionRepository, db_manager=db_manager)

    employee_service = providers.Singleton(EmployeeService, division_repository=division_repository)

    division_validator = providers.Singleton(DivisionValidator, employee_service=employee_service)

    main_window = providers.Singleton(MainWindow)
    main_menu_window = providers.Singleton(MainMenuWindow)

    report_container = providers.Container(
        ReportSessionContainer,
        employee_service=employee_service,
        division_validator=division_validator,
    )

    app_coordinator = providers.Singleton(
        AppCoordinator,
        main_window=main_window,
        main_menu_window=main_menu_window,
        session_reports_factory=report_container.provided.reports_coordinator,
    )
