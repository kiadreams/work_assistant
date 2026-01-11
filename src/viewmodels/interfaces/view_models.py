from typing import Protocol

from PySide6.QtCore import SignalInstance

from src.core.models.domain_models import DivisionDomain


class BaseViewModelProtocol(Protocol):
    data_changed_signal: SignalInstance

    def init_model_data(self) -> None: ...


class DivisionViewModelProtocol(BaseViewModelProtocol, Protocol):
    change_current_division_signal: SignalInstance

    @property
    def divisions(self) -> list[DivisionDomain]: ...

    @divisions.setter
    def divisions(self, value: list[DivisionDomain]) -> None: ...

    def load_all_divisions(self) -> None: ...

    @property
    def current_division(self) -> DivisionDomain | None: ...

    @current_division.setter
    def current_division(self, division: DivisionDomain | None) -> None: ...

    @property
    def can_delete_current_division(self) -> bool: ...

    @property
    def can_edit_current_division(self) -> bool: ...

    @property
    def can_show_all_divisions(self) -> bool: ...

    def change_current_division(self, division_name: str) -> None: ...
