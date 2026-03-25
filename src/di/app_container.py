from __future__ import annotations

from dependency_injector import containers, providers

from src.core.services import CompanyService
from src.core.services.department_service import DepartmentService
from src.core.services.division_service import DivisionService
from src.di.report_container import ReportSessionContainer
from src.gui.coordinators.app_coordinator import AppCoordinator
from src.gui.views import MainMenuWindow, MainWindow
from src.infrastucture.database import DatabaseManager
from src.infrastucture.database.repositories import CompanyRepository
from src.infrastucture.database.repositories.division import DivisionRepository


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_manager = providers.Singleton(DatabaseManager)

    company_repository = providers.Singleton(CompanyRepository, db_manager=db_manager)
    division_repository = providers.Singleton(DivisionRepository, db_manager=db_manager)
    department_repository = providers.Singleton(DivisionRepository, db_manager=db_manager)

    company_service = providers.Singleton(CompanyService, company_repository=company_repository)
    division_service = providers.Singleton(DivisionService, division_repository=division_repository)
    department_service = providers.Singleton(
        DepartmentService, department_repository=department_repository
    )

    main_window = providers.Singleton(MainWindow)
    main_menu_window = providers.Singleton(MainMenuWindow)

    report_container = providers.Factory(
        ReportSessionContainer,
        company_service=company_service,
        division_service=division_service,
        department_service=department_service,
    )

    app_coordinator = providers.Singleton(
        AppCoordinator,
        main_window=main_window,
        main_menu_window=main_menu_window,
        session_reports_factory=report_container.provider,
    )
