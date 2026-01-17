from __future__ import annotations

from typing import TYPE_CHECKING, Any, ContextManager, Protocol

if TYPE_CHECKING:
    from src.core.models.domain_models import DivisionDomain


class DatabaseManagerProtocol(Protocol):
    def create_db_tables(self) -> None: ...

    def session_scope(self) -> ContextManager[Any]: ...


class DivisionRepositoryProtocol(Protocol):
    def get_division_by_id(self, division_id: int) -> DivisionDomain | None: ...

    @property
    def all_divisions(self) -> list[DivisionDomain]: ...

    def add_new_division(self, division: DivisionDomain) -> None: ...
