from dishka import Container, make_container

from src.di.providers import (
    CoordinatorsProvider,
    DatabaseProvider,
    FactoriesProvider,
    ServiceProvider,
    UIWindowsProvider,
    ViewmodelProvider,
)


def get_container() -> Container:
    return make_container(
        DatabaseProvider(),
        ServiceProvider(),
        ViewmodelProvider(),
        UIWindowsProvider(),
        CoordinatorsProvider(),
        FactoriesProvider(),
    )
