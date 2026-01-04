from typing import Protocol, ContextManager
from dishka import Container


class OperationInvokerProtocol(Protocol):
    """
    Протокол для выполнения операций в коротком Scope.REQUEST.
    """

    _root_container: Container

    def request_container(self) -> ContextManager[Container]: ...
