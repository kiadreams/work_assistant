from PySide6.QtCore import QObject, Signal

from src.core.models.division_domain import DivisionDomain
from src.services.interfaces.services import EmployeeServiceProtocol


class DivisionViewModel(QObject):
    data_changed_signal = Signal()

    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        super().__init__()
        self._employee_service = employee_service
        self.__divisions: list[DivisionDomain] = []
        self.__current_division: DivisionDomain | None = None
        self.init_model_data()

    def init_model_data(self) -> None:
        self.load_all_divisions()
        self.__current_division = self.first_division

    @property
    def divisions(self) -> list[DivisionDomain]:
        return self.__divisions

    @divisions.setter
    def divisions(self, value: list[DivisionDomain]) -> None:
        self.__divisions = value
        self.data_changed_signal.emit()

    @property
    def current_division(self) -> DivisionDomain | None:
        if self.__current_division:
            return self.__current_division
        return None

    @current_division.setter
    def current_division(self, value: DivisionDomain) -> None:
        self.__current_division = value

    def load_all_divisions(self) -> None:
        divisions = self._employee_service.load_all_divisions()
        print(divisions)
        self.divisions = divisions

    def add_new_division(self, division_data: tuple[str, str]) -> None:
        name, full_name = division_data
        division = DivisionDomain(name=name, full_name=full_name)
        self.divisions.append(division)
        self._employee_service.add_new_division(division)

    @property
    def first_division(self) -> DivisionDomain | None:
        if self.__divisions:
            return self.__divisions[0]
        return None

    @property
    def is_current_division_deleted(self) -> bool:
        if self.__current_division is None:
            return False
        return self._employee_service.is_division_deleted(self.__current_division)

    def choose_current_division(self, division_name: str) -> None:
        division_names = [division.name for division in self.__divisions]
        if division_name in division_names:
            self.__current_division = [
                division for division in self.__divisions if division.name == division_name
            ][0]

    def delete_current_division(self) -> None:
        if self.__current_division is not None and self.is_current_division_deleted:
            self.__divisions.remove(self.__current_division)
            self._employee_service.delete_division(self.__current_division)
