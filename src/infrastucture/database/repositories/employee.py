from __future__ import annotations

from sqlalchemy import select

from src.core.exceptions.db_exceptions import DepartmentNotFoundError, DivisionNotFoundError
from src.core.interfaces.repositories import EmployeeRepositoryProtocol
from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain
from src.infrastucture.database import DatabaseManager
from src.infrastucture.database.config import DbCollFunc
from src.infrastucture.database.dto import DbDepartmentDto, DbDivisionDto
from src.infrastucture.database.entities import Department, Division


class EmployeeRepository(EmployeeRepositoryProtocol):
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    @property
    def all_divisions(self) -> list[DivisionDomain]:
        stmt = select(Division).order_by(Division.name.asc())
        with self.db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            divisions_dto = [DbDivisionDto.model_validate(d) for d in orm_result]
        return [division_dto.to_domain() for division_dto in divisions_dto]

    def is_division_name_exists(self, name: str) -> bool:
        stmt = select(Division).where(Division.name.collate(DbCollFunc.NO_CASE.value) == name)
        with self.db_manager.session_scope() as session:
            orm_division = session.execute(stmt).scalar_one_or_none()
        if orm_division is None:
            return False
        return True

    def is_department_name_exists(self, name: str) -> bool:
        stmt = select(Division).where(Division.name == name)
        with self.db_manager.session_scope() as session:
            orm_department = session.execute(stmt).scalar_one_or_none()
        if orm_department is None:
            return False
        return True

    def add_new_division(self, division: DivisionDomain) -> DivisionDomain:
        with self.db_manager.session_scope() as session:
            orm_division = Division.from_domain(division)
            session.add(orm_division)
        division_dto = DbDivisionDto.model_validate(orm_division)
        return division_dto.to_domain()

    def add_new_department(self, department: DepartmentDomain) -> DepartmentDomain:
        with self.db_manager.session_scope() as session:
            orm_department = Department.from_domain(department)
            session.add(orm_department)
        department_dto = DbDepartmentDto.model_validate(orm_department)
        return department_dto.to_domain()

    def edit_division_by_id(self, division_id: int, division: DivisionDomain) -> DivisionDomain:
        with self.db_manager.session_scope() as session:
            orm_division = session.get(Division, division_id)
            if orm_division is None:
                raise DivisionNotFoundError(division_id)
            orm_division.name = division.name
            orm_division.full_name = division.full_name
        division_dto = DbDivisionDto.model_validate(orm_division)
        return division_dto.to_domain()

    def edit_department_by_id(
        self, department_id: int, department: DepartmentDomain
    ) -> DepartmentDomain:
        with self.db_manager.session_scope() as session:
            orm_department = session.get(Department, department_id)
            if orm_department is None:
                raise DepartmentNotFoundError(department_id)
            orm_department.name = department.name
            orm_department.full_name = department.full_name
        department_dto = DbDepartmentDto.model_validate(orm_department)
        return department_dto.to_domain()

    def delete_division_by_id(self, division_id: int) -> None:
        with self.db_manager.session_scope() as session:
            orm_division = session.get(Division, division_id)
            if orm_division is None:
                raise DivisionNotFoundError(division_id)
            session.delete(orm_division)

    def delete_department_by_id(self, department_id: int) -> None:
        with self.db_manager.session_scope() as session:
            orm_department = session.get(Department, department_id)
            if orm_department is None:
                raise DepartmentNotFoundError(department_id)
            session.delete(orm_department)
