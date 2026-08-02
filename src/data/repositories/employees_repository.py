from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.data.config import DbCollFunc
from src.data.entities import Company, Department, Division, Employee, EmployeePosition
from src.domain.models import CompanyDomain, DepartmentDomain, DivisionDomain, EmployeeDomain

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
                CompanyDomain(id=c.id, name=c.name, full_name=c.full_name) for c in orm_result
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

    def get_company_divisions(self, company_id: int) -> list[DivisionDomain]:
        stmt = select(Division).order_by(Division.name.asc())
        with self._db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            divisions_dmn = [
                DivisionDomain(id=d.id, name=d.name, company_id=d.company_id, full_name=d.full_name)
                for d in orm_result
            ]
        return divisions_dmn

    def get_division_departments(self, division_id: int) -> list[DepartmentDomain]:
        stmt = (
            select(Department)
            .where(Department.division_id == division_id)
            .order_by(Department.name.asc())
        )
        with self._db_manager.session_scope() as session:
            orm_result = session.execute(stmt).scalars()
            departments_dmn = [
                DepartmentDomain(
                    id=d.id, name=d.name, full_name=d.full_name, division_id=d.division_id
                )
                for d in orm_result
            ]
        return departments_dmn

    def get_division_employees(self, division_id: int) -> list[EmployeeDomain]:
        smt = (
            select(Employee)
            .options(joinedload(Employee.employee_position))
            .join(EmployeePosition, Employee.employee_position_id == EmployeePosition.id)
            .where(EmployeePosition.division_id == division_id)
            .order_by(Employee.name.asc())
        )
        with self._db_manager.session_scope() as session:
            orm_result = session.execute(smt).scalars()
            employees_dmn = [
                EmployeeDomain(
                    id=employee.id,
                    name=employee.name,
                    last_name=employee.last_name,
                    middle_name=employee.middle_name,
                    employee_position=employee.employee_position.name,
                    employee_position_id=employee.employee_position_id,
                    service_number=employee.service_number,
                    date_of_birth=employee.date_of_birth,
                )
                for employee in orm_result
            ]
        return employees_dmn

    def get_department_employees(self, department_id: int) -> list[EmployeeDomain]:
        smt = (
            select(Employee)
            .options(joinedload(Employee.employee_position))
            .join(EmployeePosition, Employee.employee_position_id == EmployeePosition.id)
            .where(EmployeePosition.department_id == department_id)
            .order_by(Employee.name.asc())
        )
        with self._db_manager.session_scope() as session:
            orm_result = session.execute(smt).scalars()
            employees_dmn = [
                EmployeeDomain(
                    id=employee.id,
                    name=employee.name,
                    last_name=employee.last_name,
                    middle_name=employee.middle_name,
                    employee_position=employee.employee_position.name,
                    employee_position_id=employee.employee_position_id,
                    service_number=employee.service_number,
                    date_of_birth=employee.date_of_birth,
                )
                for employee in orm_result
            ]
        return employees_dmn
