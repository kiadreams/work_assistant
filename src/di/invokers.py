from contextlib import contextmanager
from typing import Generator

from dishka import Container, Scope


class OperationInvoker:
    def __init__(self, root_container: Container):
        self._root_container = root_container

    @contextmanager
    def request_container(self) -> Generator[Container, None, None]:
        with self._root_container(scope=Scope.REQUEST) as request_container:
            yield request_container
