from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data import DatabaseManager


class Factory:
    def __init__(
        self, db_connect: DatabaseManager
    ) -> None:
        self.db_connect = db_connect
