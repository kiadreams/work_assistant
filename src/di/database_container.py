from dependency_injector import containers, providers

from infrastucture.database import DatabaseManager
from infrastucture.database.repositories import DivisionRepository


class DatabaseContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_manager = providers.Singleton(DatabaseManager)
    division_repository = providers.Singleton(DivisionRepository, db_manager=db_manager)
