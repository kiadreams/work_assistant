from __future__ import annotations

from typing import Any

from PySide6.QtCore import QObject, Signal

from src.core.exceptions import DivisionExistsError, DivisionInvalidNameError
from src.core.models.division_domain import DivisionDomain
from src.gui.dto.gui_dto_models import GuiDivisionDto
from src.gui.dto.model_pipeline_services import DivisionPipelineService
from src.shared.mappers.division_mapper_service import DivisionMapperService


class BaseDialogModel(QObject):
    close_dialog_with_data_signal = Signal(Any)
    show_error_signal = Signal(str)

    def init_model_data(self) -> None:
        pass

    def validate_accepted_data_dialog(self, division_data: dict[str, str]) -> None:
        pass


class BaseDivisionDialogModel(BaseDialogModel):
    close_dialog_with_data_signal = Signal(DivisionDomain)

    def __init__(self, division_pipeline_service: DivisionPipelineService) -> None:
        super().__init__()
        self._division_pipeline_service = division_pipeline_service

    def validate_accepted_data_dialog(self, division_data: dict[str, str]) -> None:
        division: DivisionDomain | None = None
        try:
            division = self._division_pipeline_service.process_raw_data_to_domain(division_data)
        except DivisionInvalidNameError as e:
            self.show_error_signal.emit(f"{e}")
        except DivisionExistsError as e:
            self.show_error_signal.emit(f"{e}")
        if division:
            self.close_dialog_with_data_signal.emit(division)


class AddDivisionDialogModel(BaseDivisionDialogModel):
    def __init__(self, division_pipeline_service: DivisionPipelineService):
        super().__init__(division_pipeline_service)


class EditDivisionDialogModel(BaseDivisionDialogModel):
    set_current_division_data_signal = Signal(GuiDivisionDto)

    def __init__(
        self,
        division_pipeline_service: DivisionPipelineService,
        division_mapper_service: DivisionMapperService,
        current_division: DivisionDomain,
    ) -> None:
        super().__init__(division_pipeline_service)
        self._mapper = division_mapper_service
        self._current_division = current_division

    def init_model_data(self) -> None:
        division_dto = GuiDivisionDto.model_validate(self._current_division.model_data)
        print(division_dto)
        # division_dto = self._mapper.get_gui_division_dto(self._current_division)
        # self.set_current_division_data_signal.emit(division_dto)
