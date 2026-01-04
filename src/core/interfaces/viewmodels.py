from typing import Protocol

from .invokers import OperationInvokerProtocol
from ...core.models.division_domain import DivisionDomain


class BaseViewModelProtocol(Protocol):
    def init_model_data(self) -> None: ...


class DivisionViewModelProtocol(BaseViewModelProtocol, Protocol):
    _operation_invoker: OperationInvokerProtocol

    @property
    def current_service(self) -> str: ...

    @property
    def divisions(self) -> list[str]: ...

    def show_all_divisions(self) -> None: ...

    def add_new_division(self, service_data: tuple[str, str]) -> None: ...

    @property
    def first_division(self) -> DivisionDomain | None: ...

    @property
    def is_current_division_deleted(self) -> bool: ...

    def choose_current_division(self, division_name: str) -> None: ...

    def delete_current_division(self) -> None: ...
