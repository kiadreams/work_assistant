from PySide6.QtCore import QObject, Signal

from src.core.models.domain_models import DivisionDomain
from src.services.interfaces.services import EmployeeServiceProtocol


class DivisionViewModel(QObject):
    data_changed_signal = Signal()
    change_current_division_signal = Signal()

    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        super().__init__()
        self._employee_service = employee_service
        self.__divisions: list[DivisionDomain] = []
        self.__current_division: DivisionDomain | None = None

    def init_model_data(self) -> None:
        self.load_all_divisions()
        if self.__divisions:
            self.current_division = self.__divisions[0]

    @property
    def divisions(self) -> list[DivisionDomain]:
        return self.__divisions

    @divisions.setter
    def divisions(self, value: list[DivisionDomain]) -> None:
        self.__divisions = value
        self.data_changed_signal.emit()

    @property
    def current_division(self) -> DivisionDomain | None:
        return self.__current_division

    @current_division.setter
    def current_division(self, division: DivisionDomain | None) -> None:
        self.__current_division = division
        self.change_current_division_signal.emit()

    @property
    def can_delete_current_division(self) -> bool:
        if self.__current_division:
            return True
        return False

    @property
    def can_edit_current_division(self) -> bool:
        if self.__current_division:
            return True
        return False

    @property
    def can_show_all_divisions(self) -> bool:
        if self.__divisions:
            return True
        return False

    def load_all_divisions(self) -> None:
        divisions = self._employee_service.load_all_divisions()
        self.divisions = divisions

    def change_current_division(self, division_name: str) -> None:
        division = next((d for d in self.__divisions if d.name == division_name), None)
        self.current_division = division
