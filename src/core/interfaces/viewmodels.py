from typing import Protocol

from ...core.models.division_domain import DivisionDomain
from .invokers import OperationInvokerProtocol


class BaseViewModelProtocol(Protocol):
    def init_model_data(self) -> None: ...


class DivisionViewModelProtocol(BaseViewModelProtocol, Protocol):
    _operation_invoker: OperationInvokerProtocol

    @property
    def current_division(self) -> DivisionDomain | None: ...

    @property
    def divisions(self) -> list[DivisionDomain]: ...

    def load_all_divisions(self) -> None: ...

    def add_new_division(self, service_data: tuple[str, str]) -> None: ...

    @property
    def first_division(self) -> DivisionDomain | None: ...

    @property
    def is_current_division_deleted(self) -> bool: ...

    def choose_current_division(self, division_name: str) -> None: ...

    def delete_current_division(self) -> None: ...
