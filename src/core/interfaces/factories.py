from typing import Protocol, ContextManager

from dishka import Container

from src.core.interfaces.coordinators import ReportsCoordinatorProtocol
from src.core.interfaces.ui import (
    MainWindowViewProtocol,
    MainMenuViewProtocol,
    ReportsWindowViewProtocol,
)


class AppFactoryProtocol(Protocol):
    """
    Протокол фабрики для создания окон и вспомогательных координаторов.
    """

    _root_container: Container

    @property
    def main_window(self) -> MainWindowViewProtocol: ...

    @property
    def main_menu(self) -> MainMenuViewProtocol: ...

    @property
    def reports_window(self) -> ReportsWindowViewProtocol: ...

    def start_reports_session(self) -> ContextManager[ReportsCoordinatorProtocol]: ...
