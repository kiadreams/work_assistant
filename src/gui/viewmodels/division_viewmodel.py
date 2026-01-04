from dishka import Container

from ...core.interfaces.invokers import OperationInvokerProtocol
from ...core.interfaces.services import EmployeeServiceProtocol
from ...core.models.division_domain import DivisionDomain


class DivisionViewModel:
    def __init__(self, operation_invoker: OperationInvokerProtocol) -> None:
        self._operation_invoker = operation_invoker
        self.company = "Кубанское ПМЭС"
        self.__divisions: list[DivisionDomain] = []
        self.__current_division: DivisionDomain | None = None

    def init_model_data(self) -> None:
        self.show_all_divisions()
        self.__current_division = self.first_division

    @property
    def current_service(self) -> str:
        if self.__current_division is not None:
            return str(self.__current_division.name)
        else:
            return ""

    @property
    def divisions(self) -> list[str]:
        return [service.name for service in self.__divisions]

    def show_all_divisions(self) -> None:
        with self._operation_invoker.request_container() as container:
            employee_service = container.get(EmployeeServiceProtocol)
            self.__divisions = employee_service.load_all_divisions()

    def add_new_division(self, service_data: tuple[str, str]) -> None:
        name, full_name = service_data
        division = DivisionDomain(name=name, full_name=full_name)
        self.__divisions.append(division)
        with self._operation_invoker.request_container() as container:
            employee_service = container.get(EmployeeServiceProtocol)
            employee_service.save_division(division)

    @property
    def first_division(self) -> DivisionDomain | None:
        if self.__divisions:
            return self.__divisions[0]
        return None

    @property
    def is_current_division_deleted(self) -> bool:
        if self.__current_division is None:
            return False
        with self._operation_invoker.request_container() as container:
            employee_service = container.get(EmployeeServiceProtocol)
            return employee_service.is_division_deleted(self.__current_division)  # type: ignore[no-any-return]

    def choose_current_division(self, division_name: str) -> None:
        division_names = [division.name for division in self.__divisions]
        if division_name in division_names:
            self.__current_division = [
                division for division in self.__divisions if division.name == division_name
            ][0]

    def delete_current_division(self) -> None:
        if self.__current_division is not None and self.is_current_division_deleted:
            self.__divisions.remove(self.__current_division)
            with self._operation_invoker.request_container() as container:
                employee_service = container.get(EmployeeServiceProtocol)
                employee_service.delete_division(self.__current_division)
