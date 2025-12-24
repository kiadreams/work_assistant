from sqlalchemy import select

from .base_viewmodel import BaseViewModel
from ..entities.division import Division


class DivisionViewModel(BaseViewModel):
    def __init__(self, company: str):
        super().__init__()
        self.company = company
        self.__services: list[Division] = []
        self.__current_service: Division | None = None
        self._init_model_data()

    def _init_model_data(self) -> None:
        self.load_all_services()
        self.set_first_service()

    @property
    def current_service(self) -> str:
        if self.__current_service is not None:
            return str(self.__current_service.name)
        else:
            return ""

    @property
    def services(self) -> list[str]:
        return [service.name for service in self.__services]

    def load_all_services(self) -> None:
        stmt = select(Division)
        self.__services = list(self.session.execute(stmt).scalars().all())

    def add_new_service(self, service_data: tuple[str, str]) -> None:
        name, full_name = service_data
        service = Division(name=name, full_name=full_name)
        self.session.add(service)
        self.session.commit()

    def set_first_service(self) -> None:
        if self.__services:
            self.__current_service = self.__services[0]

    def can_delete_current_division(self) -> bool:
        if self.__current_service is None:
            return False
        elif self.__current_service.departments or self.__current_service.employee_positions:
            return False
        else:
            return True

    def change_current_division(self, service_name: str) -> None:
        if service_name in self.services:
            self.__current_service = [
                service for service in self.__services if service.name == service_name
            ][0]

    def delete_current_division(self) -> None:
        if self.__current_service is not None:
            self.session.delete(self.__current_service)
            self.session.commit()
            self.__services.remove(self.__current_service)
            self.set_first_service()
