from __future__ import annotations

from typing import TYPE_CHECKING

from config import DbCollFunc
from sqlalchemy import select

if TYPE_CHECKING:
    from entities import Company
    from mappers.staff_mapper import StaffMapper

    from domain.models import CompanyDomain
    from src.data import DatabaseManager


class CompanyRepository:
    def __init__(self, db_manager: DatabaseManager, staff_mapper: StaffMapper) -> None:
        self.db_manager = db_manager
        self.mapper = staff_mapper

    @property
    def all_companies(self) -> list[CompanyDomain]:
        stmt = select(Company).order_by(Company.name.asc())
        with self.db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            companies_dmn = [
                CompanyDomain(company_id=c.id, name=c.name, full_name=c.full_name)
                for c in orm_result
            ]
        return companies_dmn

    def is_company_name_exists(self, name: str) -> bool:
        stmt = select(Company).where(Company.name.collate(DbCollFunc.NO_CASE.value) == name)
        with self.db_manager.session_scope() as session:
            orm_company = session.execute(stmt).scalar_one_or_none()
        if orm_company is None:
            return False
        return True

    def add_new_company(self, company: CompanyDomain) -> CompanyDomain:
        with self.db_manager.session_scope() as session:
            company_orm = Company.from_domain(company)
            session.add(company_orm)
            company_dmn = CompanyDomain(
                company_id=company_orm.id, name=company_orm.name, full_name=company_orm.full_name
            )
        return company_dmn
