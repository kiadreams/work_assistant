from __future__ import annotations

from PySide6.QtCore import QObject, Signal

from src.core.exceptions import DivisionExistsError, DivisionInvalidNameError
from src.core.models.division_domain import DivisionDomain
from src.gui.dto.model_pipeline_services import DivisionPipelineService


class EditDivisionDialogModel(QObject):
    close_dialog_with_data_signal = Signal(DivisionDomain)
    show_error_signal = Signal(str)

    def __init__(self, division_pipeline_service: DivisionPipelineService):
        super().__init__()
        self.division_pipeline_service = division_pipeline_service
        self._current_division: DivisionDomain | None = None

    def validate_accepted_data_dialog(self, division_data: dict[str, str]) -> None:
        division: DivisionDomain | None = None
        try:
            division = self.division_pipeline_service.process_raw_data_to_domain(division_data)
        except DivisionInvalidNameError as e:
            self.show_error_signal.emit(f"{e}")
        except DivisionExistsError as e:
            self.show_error_signal.emit(f"{e}")
        if division:
            self.close_dialog_with_data_signal.emit(division)
