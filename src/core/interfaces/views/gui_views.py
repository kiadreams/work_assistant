from typing import Protocol


class MainWindowProtocol(Protocol):
    def add_window(self) -> None: ...
