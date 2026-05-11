from __future__ import annotations

from sqlalchemy import select

from src.core.interfaces.repositories import CompanyRepositoryProtocol
from src.core.models.company_domain import CompanyDomain
from src.infrastucture.database import DatabaseManager
from src.infrastucture.database.config import DbCollFunc
from src.infrastucture.database.dto.models import DbCompanyDto
from src.infrastucture.database.entities.company import Company


class CompanyRepository(CompanyRepositoryProtocol):
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    @property
    def all_companies(self) -> list[CompanyDomain]:
        stmt = select(Company).order_by(Company.name.asc())
        with self.db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            companies_dto = [DbCompanyDto.model_validate(c) for c in orm_result]
        return [company_dto.to_domain() for company_dto in companies_dto]

    def is_company_name_exists(self, name: str) -> bool:
        stmt = select(Company).where(Company.name.collate(DbCollFunc.NO_CASE.value) == name)
        with self.db_manager.session_scope() as session:
            orm_company = session.execute(stmt).scalar_one_or_none()
        if orm_company is None:
            return False
        return True

    def add_new_company(self, company: CompanyDomain) -> CompanyDomain:
        with self.db_manager.session_scope() as session:
            orm_company = Company.from_domain(company)
            session.add(orm_company)
            session.flush()
            company_dto = DbCompanyDto.model_validate(orm_company)
        return company_dto.to_domain()
