from src.core.interfaces.repositories import DivisionRepositoryProtocol
from src.core.models.division_domain import DivisionDomain


class DivisionService:
    def __init__(self, division_repository: DivisionRepositoryProtocol) -> None:
        self._repository = division_repository

    def is_division_name_exists(self, division_name: str) -> bool:
        name_is_exist = self._repository.is_division_name_exists(division_name)
        return name_is_exist

    def load_all_divisions(self) -> list[DivisionDomain]:
        divisions = self._repository.all_divisions
        return divisions

    def load_division_by_id(self, division_id: int) -> DivisionDomain:
        return self._repository.get_division_by_id(division_id)

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
