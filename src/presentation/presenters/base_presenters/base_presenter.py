from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.coordinators.main_window_coordinator import MainWindowCoordinator


class BasePresenter:
    def __init__(
        self,
        main_coordinator: MainWindowCoordinator,
        widget_index: int,
    ) -> None:
        self.coordinator = main_coordinator
        self.widget_index = widget_index

    def start(self) -> None:
        pass

    def teardown(self) -> None:
        pass
