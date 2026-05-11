from __future__ import annotations

from sqlalchemy import select

from src.core.exceptions.db_exceptions import DivisionNotFoundError
from src.core.interfaces.repositories import DivisionRepositoryProtocol
from src.core.models.division_domain import DivisionDomain
from src.infrastucture.database import DatabaseManager
from src.infrastucture.database.config import DbCollFunc
from src.infrastucture.database.dto import DbDivisionDto
from src.infrastucture.database.entities import Division


class DivisionRepository(DivisionRepositoryProtocol):
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    @property
    def get_company_divisions(self) -> list[DivisionDomain]:
        stmt = select(Division).order_by(Division.name.asc())
        with self.db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            divisions_dto = [DbDivisionDto.model_validate(d) for d in orm_result]
        return [division_dto.to_domain() for division_dto in divisions_dto]

    def get_division_by_id(self, division_id: int) -> DivisionDomain:
        stmt = select(Division).where(Division.id == division_id)
        with self.db_manager.session_scope() as session:
            orm_division = session.execute(stmt).scalar_one_or_none()
            if orm_division is None:
                raise DivisionNotFoundError(division_id)
            division_dto = DbDivisionDto.model_validate(orm_division)
        return division_dto.to_domain()

    def is_division_name_exists(self, name: str) -> bool:
        stmt = select(Division).where(Division.name.collate(DbCollFunc.NO_CASE.value) == name)
        with self.db_manager.session_scope() as session:
            orm_division = session.execute(stmt).scalar_one_or_none()
        if orm_division is None:
            return False
        return True

    def add_new_division(self, division: DivisionDomain) -> DivisionDomain:
        with self.db_manager.session_scope() as session:
            orm_division = Division.from_domain(division)
            session.add(orm_division)
            session.flush()
            division_dto = DbDivisionDto.model_validate(orm_division)
        return division_dto.to_domain()

    def edit_division_by_id(self, division_id: int, division: DivisionDomain) -> DivisionDomain:
        with self.db_manager.session_scope() as session:
            orm_division = session.get(Division, division_id)
            if orm_division is None:
                raise DivisionNotFoundError(division_id)
            orm_division.name = division.name
            orm_division.full_name = division.full_name
            division_dto = DbDivisionDto.model_validate(orm_division)
        return division_dto.to_domain()

    def delete_division_by_id(self, division_id: int) -> None:
        with self.db_manager.session_scope() as session:
            orm_division = session.get(Division, division_id)
            if orm_division is None:
                raise DivisionNotFoundError(division_id)
            session.delete(orm_division)
