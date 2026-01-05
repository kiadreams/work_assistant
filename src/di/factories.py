from contextlib import contextmanager
from typing import Generator

from dishka import Container, Scope

from src.core.interfaces.coordinators import ReportsCoordinatorProtocol
from src.core.interfaces.ui import (
    MainMenuViewProtocol,
    MainWindowViewProtocol,
    ReportsWindowViewProtocol,
)


class AppFactory:
    """
    Фабрика для создания окон и вспомогательных координаторов.
    """

    def __init__(self, root_container: Container) -> None:
        self._root_container = root_container

    @property
    def main_window(self) -> MainWindowViewProtocol:
        return self._root_container.get(MainWindowViewProtocol)  # type: ignore[no-any-return]

    @property
    def main_menu(self) -> MainMenuViewProtocol:
        return self._root_container.get(MainMenuViewProtocol)  # type: ignore[no-any-return]

    @property
    def reports_window(self) -> ReportsWindowViewProtocol:
        return self._root_container.get(ReportsWindowViewProtocol)  # type: ignore[no-any-return]

    @contextmanager
    def start_reports_session(self) -> Generator[ReportsCoordinatorProtocol, None, None]:
        with self._root_container(scope=Scope.SESSION) as session_container:
            yield session_container.get(ReportsCoordinatorProtocol)
