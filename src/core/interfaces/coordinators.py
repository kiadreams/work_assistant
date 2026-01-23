from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from src.gui.views.base_views import BaseView, SessionWindow


class BaseCoordinatorProtocol(Protocol):
    def start(self) -> None: ...

    def teardown(self) -> None: ...


class AppCoordinatorProtocol(BaseCoordinatorProtocol, Protocol):
    def open_main_menu_window(self) -> None: ...

    def open_reports_window(self) -> None: ...

    def open_protocols_window(self) -> None: ...


class SessionCoordinatorProtocol(BaseCoordinatorProtocol, Protocol):
    @property
    def session_window(self) -> SessionWindow: ...


class ReportsCoordinatorProtocol(SessionCoordinatorProtocol, Protocol):
    def open_divisions_view(self) -> None: ...

    def open_staff_view(self) -> None: ...

    def open_work_types_view(self) -> None: ...

    def open_works_view(self) -> None: ...

    def open_orders_view(self) -> None: ...

    def open_work_events_view(self) -> None: ...


class ProtocolsCoordinatorProtocol(SessionCoordinatorProtocol, Protocol):
    def choose_protocol_temple(self) -> None: ...


class ViewCoordinatorProtocol(BaseCoordinatorProtocol, Protocol):
    @property
    def view(self) -> BaseView: ...


class DivisionViewCoordinatorProtocol(ViewCoordinatorProtocol, Protocol):
    pass
