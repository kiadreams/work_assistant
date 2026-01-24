from __future__ import annotations

from dependency_injector import containers, providers

from src.core.services import EmployeeService
from src.di.report_container import ReportSessionContainer
from src.gui.coordinators.app_coordinator import AppCoordinator
from src.gui.views import MainMenuWindow, MainWindow
from src.infrastucture.database import DatabaseManager
from src.infrastucture.database.repositories import DivisionRepository


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_manager = providers.Singleton(DatabaseManager)

    division_repository = providers.Singleton(DivisionRepository, db_manager=db_manager)

    employee_service = providers.Singleton(EmployeeService, division_repository=division_repository)

    main_window = providers.Singleton(MainWindow)
    main_menu_window = providers.Singleton(MainMenuWindow)

    report_container = providers.Factory(
        ReportSessionContainer,
        employee_service=employee_service,
    )

    app_coordinator = providers.Singleton(
        AppCoordinator,
        main_window=main_window,
        main_menu_window=main_menu_window,
        session_reports_factory=report_container.provider,
    )
