from src.core.interfaces.repositories import DivisionRepositoryProtocol
from src.core.models.division_domain import DivisionDomain


class EmployeeService:
    def __init__(self, division_repository: DivisionRepositoryProtocol):
        self.division_repository = division_repository

    def is_division_deleted(self, division: DivisionDomain) -> bool:
        return False

    def load_all_divisions(self) -> list[DivisionDomain]:
        divisions = self.division_repository.all_divisions
        return divisions

    def add_new_division(self, division: DivisionDomain) -> None:
        pass

    def edit_division_data(self, value: str) -> None:
        pass

    def delete_division(self, division: DivisionDomain) -> None:
        pass
