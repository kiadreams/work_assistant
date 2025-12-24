from typing import Protocol


class IBaseAppWidget(Protocol):

    def setupUi(self) -> None: ...

    def setStyleSheet(self, stylesheet: str | None) -> None: ...
