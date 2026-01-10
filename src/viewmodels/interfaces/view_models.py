from typing import Protocol

from PySide6.QtCore import SignalInstance

from src.core.models.division_domain import DivisionDomain


class BaseViewModelProtocol(Protocol):
    data_changed_signal: SignalInstance

    def init_model_data(self) -> None: ...


class DivisionViewModelProtocol(BaseViewModelProtocol, Protocol):
    @property
    def divisions(self) -> list[DivisionDomain]: ...

    def load_all_divisions(self) -> None: ...
