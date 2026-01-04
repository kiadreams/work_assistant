from typing import Protocol, Any
from ..constants import PageStructure


class BaseViewProtocol(Protocol):
    def init_content_view(self) -> None: ...


class MainWindowViewProtocol(BaseViewProtocol, Protocol):
    def show(self) -> None: ...

    def close(self) -> bool: ...

    def insert_into_stacked_windows(self, index: PageStructure, window: Any) -> None: ...

    def change_page(self, index: PageStructure) -> None: ...


class MainMenuViewProtocol(BaseViewProtocol, Protocol):
    open_reports_window_signal: Any
    open_protocols_window_signal: Any
    close_app_signal: Any


class ReportsWindowViewProtocol(BaseViewProtocol, Protocol):
    back_main_menu_signal: Any

    def insert_into_stacked_windows(self, index: PageStructure, window: Any) -> None: ...

    def change_page(self, index: PageStructure) -> None: ...