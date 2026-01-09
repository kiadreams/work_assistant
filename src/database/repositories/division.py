from sqlalchemy import select

from ...core.models.division_domain import DivisionDomain
from ..entities import Division
from ..interfaces import DatabaseManagerProtocol


class DivisionRepository:
    def __init__(self, db_manager: DatabaseManagerProtocol) -> None:
        self.db_manager = db_manager

    def get_division_by_name(self, name: str) -> DivisionDomain | None:
        # stmt = select(Division).where(Division.name == name)
        return DivisionDomain(name=name, full_name=None)

    @property
    def all_divisions(self) -> list[DivisionDomain]:
        stmt = select(Division).order_by(Division.name.asc())
        with self.db_manager.session_scope() as session:
            result = session.execute(stmt).scalars()
            divisions = [DivisionDomain.model_validate(division) for division in result]
        return divisions

    def add_new_division(self, division_domain: DivisionDomain) -> None:
        # division = Division(name=division_domain.name, full_name=division_domain.full_name)
        pass
