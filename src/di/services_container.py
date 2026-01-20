from dependency_injector import containers, providers

from core.services import EmployeeService
from core.validators.division_validator import DivisionValidator
from di.database_container import DatabaseContainer


class ServiceContainer(containers.DeclarativeContainer):
    db_container = providers.Container(DatabaseContainer)
    employee_service = providers.Singleton(
        EmployeeService,
        division_repository=db_container.division_repository,
    )
    division_validator = providers.Singleton(
        DivisionValidator,
        employee_service=employee_service,
    )
