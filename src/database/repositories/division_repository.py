from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.orm import Session

from ...core.models.division_domain import DivisionDomain
from ..entities import Division


class DivisionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_division_by_name(self, name: str) -> DivisionDomain | None:
        stmt = select(Division).where(Division.name == name)
        try:
            division = self.session.scalar(stmt)
            return DivisionDomain.model_validate(division)
        except MultipleResultsFound:
            print("Найдено более одного значения division")
        return None

    @property
    def all_divisions(self) -> list[DivisionDomain]:
        stmt = select(Division).order_by(Division.name.asc())
        try:
            divisions = self.session.scalars(stmt).all()
            return [DivisionDomain.model_validate(d) for d in divisions]
        except Exception as e:
            print(f"Произошла ошибка при запросе всех служб: {e}")
            return []

    def add_new_division(self, division_domain: DivisionDomain) -> None:
        division = Division(name=division_domain.name, full_name=division_domain.full_name)
        self.session.add(division)
