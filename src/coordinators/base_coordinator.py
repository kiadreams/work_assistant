from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from di import BaseFactory


class BaseCoordinator:
    def __init__(self, factory: BaseFactory) -> None:
        self.factory = factory
