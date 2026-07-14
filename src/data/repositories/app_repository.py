from __future__ import annotations

from typing import TYPE_CHECKING

from mappers.staff_mapper import StaffMapper
from reports_repositories import CompanyRepository, DepartmentRepository, DivisionRepository

if TYPE_CHECKING:
    from src.data import DatabaseManager


class AppRepository:
    def __init__(
        self,
        *,
        db_manager: DatabaseManager,
        company_repo: CompanyRepository,
        dapartment_repo: DepartmentRepository,
        division_repo: DivisionRepository,
    ) -> None:
        self.__db_manager = db_manager
        self.__company_repository = company_repo
        self.__department_repository = None
        self.__division_repository = None
        self.__init_repositories()

    def __init_repositories(self) -> None:
        __mapper = StaffMapper()
        self.__company_repository = CompanyRepository(self.__db_manager, __mapper)
        self.__department_repository = DepartmentRepository(self.__db_manager, __mapper)
        self.__division_repository = DivisionRepository(self.__db_manager, __mapper)

    @property
    def company(self) -> CompanyRepository:
        return self.__company_repository

    @property
    def department(self) -> DepartmentRepository:
        return self.__department_repository

    @property
    def division(self) -> DivisionRepository:
        return self.__division_repository
