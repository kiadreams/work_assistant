from sqlalchemy import select

from src.core.models.domain_models import DivisionDomain
from src.database.entities import Division
from src.database.interfaces import DatabaseManagerProtocol


class DivisionRepository:
    def __init__(self, db_manager: DatabaseManagerProtocol) -> None:
        self.db_manager = db_manager

    def get_division_by_id(self, division_id: int) -> DivisionDomain | None:
        stmt = select(Division).where(Division.id == division_id)
        with self.db_manager.session_scope() as session:
            result = session.execute(stmt).scalar()
            division = DivisionDomain.model_validate(result)
        return division

    @property
    def all_divisions(self) -> list[DivisionDomain]:
        stmt = select(Division).order_by(Division.name.asc())
        with self.db_manager.session_scope() as session:
            result = session.execute(stmt).scalars()
            divisions = [DivisionDomain.model_validate(d) for d in result]
        return divisions

    def add_new_division(self, division: DivisionDomain) -> None:
        pass
