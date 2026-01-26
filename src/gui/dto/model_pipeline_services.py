from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain
from src.core.validators.division_validators import (
    DepartmentValidator,
    DivisionValidator,
)
from src.gui.dto.gui_dto_models import GuiDepartmentDto, GuiDivisionDto


class DivisionPipelineService:
    def __init__(self, division_validator: DivisionValidator):
        self._validator = division_validator

    def process_raw_data_to_domain(self, raw_data: dict[str, str]) -> DivisionDomain:
        """
        Полный конвейер валидации: формат + бизнес-логика.
        """
        division_dto = GuiDivisionDto.model_validate(raw_data)
        division = self._validator.create_division(division_dto)
        return division


class DepartmentPipelineService:
    def __init__(self, department_validator: DepartmentValidator):
        self._validator = department_validator

    def process_raw_data_to_domain(self, raw_data: dict[str, str]) -> DepartmentDomain:
        """
        Полный конвейер валидации: формат + бизнес-логика.
        """
        department_dto = GuiDepartmentDto.model_validate(raw_data)
        department = self._validator.create_department(department_dto)
        return department
