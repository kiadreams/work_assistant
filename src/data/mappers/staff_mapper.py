from src.data.entities import Company
from src.domain.models import CompanyDomain


class StaffMapper:
    @staticmethod
    def company_orm_to_domain(company_orm: Company) -> CompanyDomain:
        company_dmn = CompanyDomain(
            company_id=company_orm.id,
            name=company_orm.name,
            full_name=company_orm.full_name,
        )
        return company_dmn
