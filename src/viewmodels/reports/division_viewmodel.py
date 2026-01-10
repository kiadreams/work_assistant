from PySide6.QtCore import QObject, Signal

from src.core.models.division_domain import DivisionDomain
from src.services.interfaces.services import EmployeeServiceProtocol


class DivisionViewModel(QObject):
    data_changed_signal = Signal()

    def __init__(self, employee_service: EmployeeServiceProtocol) -> None:
        super().__init__()
        self._employee_service = employee_service
        self.__divisions: list[DivisionDomain] = []
        self.init_model_data()

    def init_model_data(self) -> None:
        self.load_all_divisions()

    @property
    def divisions(self) -> list[DivisionDomain]:
        return self.__divisions

    @divisions.setter
    def divisions(self, value: list[DivisionDomain]) -> None:
        self.__divisions = value
        self.data_changed_signal.emit()

    def load_all_divisions(self) -> None:
        divisions = self._employee_service.load_all_divisions()
        self.divisions = divisions
