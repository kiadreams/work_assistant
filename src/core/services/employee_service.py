from src.core.interfaces.repositories import EmployeeRepositoryProtocol
from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain


class EmployeeService:
    def __init__(self, division_repository: EmployeeRepositoryProtocol) -> None:
        self._repository = division_repository

    def is_division_name_exists(self, division_name: str) -> bool:
        name_is_exist = self._repository.is_division_name_exists(division_name)
        return name_is_exist

    def is_department_name_exists(self, department_name: str) -> bool:
        name_is_exist = self._repository.is_department_name_exists(department_name)
        return name_is_exist

    def load_all_divisions(self) -> list[DivisionDomain]:
        divisions = self._repository.all_divisions
        return divisions

    def add_new_division(self, division: DivisionDomain) -> DivisionDomain:
        division = self._repository.add_new_division(division)
        return division

    def edit_division_data_by_id(
        self, division_id: int, division: DivisionDomain
    ) -> DivisionDomain:
        division = self._repository.edit_division_by_id(division_id, division)
        return division

    def delete_division_by_id(self, division_id: int) -> None:
        self._repository.delete_division_by_id(division_id)

    def add_new_department(self, department: DepartmentDomain) -> DepartmentDomain:
        department = self._repository.add_new_department(department)
        return department

    def edit_department_data_by_id(
        self, department_id: int, department: DepartmentDomain
    ) -> DepartmentDomain:
        department = self._repository.edit_department_by_id(department_id, department)
        return department

    def delete_department_by_id(self, department_id: int) -> None:
        self._repository.delete_department_by_id(department_id)
