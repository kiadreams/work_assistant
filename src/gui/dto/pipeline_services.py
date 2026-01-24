from src.core.models.division_domain import DivisionDomain
from src.core.validators.division_validator import (
    DivisionValidator,
)
from src.gui.dto.models import DivisionDto


class DivisionPipelineService:
    def __init__(self, division_validator: DivisionValidator):
        self._core_validator = division_validator

    def process_raw_data_to_domain(self, raw_data: dict[str, str]) -> DivisionDomain:
        """
        Полный конвейер валидации: формат + бизнес-логика.
        """
        division_dto = DivisionDto.model_validate(raw_data)
        division = self._core_validator.create_division(division_dto)
        return division
