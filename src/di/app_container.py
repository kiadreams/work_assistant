from dependency_injector import containers, providers

from di.database_container import DatabaseContainer
from di.services_container import ServiceContainer
from di.viewmodels_container import ViewModelsContainer


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    database_layer = providers.Container(DatabaseContainer, config=config)
    services_layer = providers.Container(ServiceContainer)
    view_models_layer = providers.Container(ViewModelsContainer)
