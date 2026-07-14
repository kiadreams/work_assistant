from mappers import StaffMapper
from reports_repositories import CompanyRepository, DepartmentRepository, DivisionRepository
from repositories import AppRepository

from data import DatabaseManager


def create_app_repository() -> AppRepository:
    db_manager = DatabaseManager()
    staff_mapper = StaffMapper()
    company_repository = CompanyRepository()
    department_repository = DepartmentRepository()
    division_repository = DivisionRepository()
    app_repository = AppRepository(

    )