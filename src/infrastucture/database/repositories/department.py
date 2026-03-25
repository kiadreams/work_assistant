from __future__ import annotations

from sqlalchemy import select

from src.core.exceptions.db_exceptions import DepartmentNotFoundError
from src.core.interfaces.repositories import DepartmentRepositoryProtocol
from src.core.models.department_domain import DepartmentDomain
from src.infrastucture.database import DatabaseManager
from src.infrastucture.database.dto import DbDepartmentDto
from src.infrastucture.database.entities import Department, Division


class DepartmentRepository(DepartmentRepositoryProtocol):
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    @property
    def all_departments(self) -> list[DepartmentDomain]:
        stmt = select(Department).order_by(Department.name.asc())
        with self.db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            departments_dto = [DbDepartmentDto.model_validate(d) for d in orm_result]
        return [department_dto.to_domain() for department_dto in departments_dto]

    def is_department_name_exists(self, name: str) -> bool:
        stmt = select(Division).where(Division.name == name)
        with self.db_manager.session_scope() as session:
            orm_department = session.execute(stmt).scalar_one_or_none()
        if orm_department is None:
            return False
        return True

    def add_new_department(self, department: DepartmentDomain) -> DepartmentDomain:
        with self.db_manager.session_scope() as session:
            orm_department = Department.from_domain(department)
            session.add(orm_department)
            session.flush()
            department_dto = DbDepartmentDto.model_validate(orm_department)
        return department_dto.to_domain()

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

    def delete_department_by_id(self, department_id: int) -> None:
        with self.db_manager.session_scope() as session:
            orm_department = session.get(Department, department_id)
            if orm_department is None:
                raise DepartmentNotFoundError(department_id)
            session.delete(orm_department)
