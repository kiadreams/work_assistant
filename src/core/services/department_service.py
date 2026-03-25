from src.core.interfaces.repositories import DepartmentRepositoryProtocol
from src.core.models.department_domain import DepartmentDomain


class DepartmentService:
    def __init__(self, department_repository: DepartmentRepositoryProtocol) -> None:
        self._repository = department_repository

    def is_department_name_exists(self, department_name: str) -> bool:
        name_is_exist = self._repository.is_department_name_exists(department_name)
        return name_is_exist

    def load_all_departments(self) -> list[DepartmentDomain]:
        departments = self._repository.all_departments
        return departments

    def load_department_by_id(self, department_id: int) -> DepartmentDomain:
        return self._repository.get_department_by_id(department_id)

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
