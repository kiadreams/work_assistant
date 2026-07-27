from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select

from src.data.config import DbCollFunc
from src.data.entities.company import Company
from src.domain.models import CompanyDomain

if TYPE_CHECKING:
    from src.data import DatabaseManager


class EmployeesRepository:
    def __init__(self, db_manager: DatabaseManager) -> None:
        self._db_manager = db_manager

    def get_all_companies(self) -> list[CompanyDomain]:
        stmt = select(Company).order_by(Company.name.asc())
        with self._db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            companies_dmn = [
                CompanyDomain(company_id=c.id, name=c.name, full_name=c.full_name)
                for c in orm_result
            ]
        return companies_dmn

    def is_company_name_exists(self, name: str) -> bool:
        stmt = select(Company).where(Company.name.collate(DbCollFunc.NO_CASE.value) == name)
        with self._db_manager.session_scope() as session:
            orm_company = session.execute(stmt).scalar_one_or_none()
        if orm_company is None:
            return False
        return True

    def is_company_id_exists(self, company_id: int) -> bool:
        stmt = select(Company).where(Company.id == company_id)
        with self._db_manager.session_scope() as session:
            orm_company = session.execute(stmt).scalar_one_or_none()
        if orm_company is None:
            return False
        return True

    # def add_new_company(self, company: CompanyDomain) -> CompanyDomain:
    #     with self._db_manager.session_scope() as session:
    #         company_orm = Company.from_domain(company)
    #         session.add(company_orm)
    #     company_dmn = CompanyDomain(
    #         company_id=company_orm.id, name=company_orm.name, full_name=company_orm.full_name
    #     )
    #     return company_dmn
