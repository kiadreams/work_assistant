from sqlalchemy import select

from src.core.interfaces.repositories import DatabaseManagerProtocol, DivisionRepositoryProtocol
from src.core.models.division_domain import DivisionDomain
from src.infrastucture.database.dto import DbDivisionDto
from src.infrastucture.database.entities import Division


class DivisionRepository(DivisionRepositoryProtocol):
    def __init__(self, db_manager: DatabaseManagerProtocol) -> None:
        self.db_manager = db_manager

    def get_division_by_id(self, division_id: int) -> DivisionDomain | None:
        stmt = select(Division).where(Division.id == division_id)
        with self.db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalar()
            division_dto = DbDivisionDto.model_validate(orm_result)
        return DivisionDomain.division_from_data(division_dto)

    @property
    def all_divisions(self) -> list[DivisionDomain]:
        stmt = select(Division).order_by(Division.name.asc())
        with self.db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            divisions_dto = [DbDivisionDto.model_validate(d) for d in orm_result]
        return [DivisionDomain.division_from_data(division_dto) for division_dto in divisions_dto]

    def add_new_division(self, division: DivisionDomain) -> None:
        pass
