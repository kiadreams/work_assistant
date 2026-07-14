from __future__ import annotations

from typing import TYPE_CHECKING

from mappers.staff_mapper import StaffMapper
from reports_repositories import CompanyRepository, DepartmentRepository, DivisionRepository

if TYPE_CHECKING:


    from src.data import DatabaseManager


class AppRepository:
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager
        self._company_repository = None
        self._department_repository = None
        self._division_repository = None
        self.__init_repositories()

    def __init_repositories(self) -> None:
        __mapper = StaffMapper()
        self._company_repository = CompanyRepository(self.db_manager, __mapper)
        self._department_repository = DepartmentRepository(self.db_manager, __mapper)
        self._division_repository = DivisionRepository(self.db_manager, __mapper)

    @property
    def company(self) -> CompanyRepository:
        return self._company_repository

    @property
    def department(self) -> DepartmentRepository:
        return self._department_repository

    @property
    def division(self) -> DivisionRepository:
        return self._division_repository
