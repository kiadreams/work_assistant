from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from di import Factory


class Coordinator:
    def __init__(self, factory: Factory) -> None:
        self.factory = factory
