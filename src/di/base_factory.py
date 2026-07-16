from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data import DatabaseManager


class BaseFactory:
    def __init__(
        self, db_manager: DatabaseManager
    ) -> None:
        self.db_client = db_manager
