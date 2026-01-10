from typing import Protocol

from PySide6.QtWidgets import QWidget

from gui.interfaces.views import BaseViewProtocol
from src.gui.interfaces.views import SessionWindowProtocol


class AppCoordinatorProtocol(Protocol):
    def start_app(self) -> None: ...

    def open_main_menu_window(self) -> None: ...

    def open_reports_window(self) -> None: ...

    def open_protocols_window(self) -> None: ...


class SessionCoordinatorProtocol(Protocol):
    def __start_session(self) -> None: ...

    @property
    def session_window(self) -> SessionWindowProtocol | QWidget: ...


class ReportsCoordinatorProtocol(SessionCoordinatorProtocol, Protocol):
    def open_divisions_view(self) -> None: ...

    def open_staff_view(self) -> None: ...

    def open_work_types_view(self) -> None: ...

    def open_works_view(self) -> None: ...

    def open_orders_view(self) -> None: ...

    def open_work_events_view(self) -> None: ...


class ProtocolsCoordinatorProtocol(SessionCoordinatorProtocol, Protocol):
    def choose_protocol_temple(self) -> None: ...


class ViewCoordinatorProtocol(Protocol):
    def start_view(self) -> None: ...

    @property
    def view(self) -> BaseViewProtocol | QWidget: ...

class DivisionViewCoordinatorProtocol(ViewCoordinatorProtocol, Protocol):
    pass