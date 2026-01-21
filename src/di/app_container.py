from __future__ import annotations

from dependency_injector import containers, providers

from gui.views import MainMenuWindow, MainWindow
from infrastucture.database import DatabaseManager
from infrastucture.database.repositories import DivisionRepository
from src.core.services import EmployeeService
from src.di.sessions_container import SessionsContainer
from src.gui.coordinators.app_coordinator import AppCoordinator


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_manager = providers.Singleton(DatabaseManager)

    division_repository = providers.Singleton(DivisionRepository, db_manager=db_manager)

    employee_service = providers.Singleton(EmployeeService, division_repository=division_repository)

    main_window = providers.Singleton(MainWindow)
    main_menu_window = providers.Singleton(MainMenuWindow)

    sessions_factory = providers.Singleton(
        SessionsContainer,
        employee_service=employee_service,
    )

    app_coordinator = providers.Singleton(
        AppCoordinator,
        main_window=main_window,
        main_menu_window=main_menu_window,
        sessions_factory=sessions_factory,
    )
