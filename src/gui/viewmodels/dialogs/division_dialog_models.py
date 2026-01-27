from __future__ import annotations

from PySide6.QtCore import Signal

from src.core.exceptions.business_exceptions import StructureExistsError, StructureInvalidNameError
from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain
from src.gui.dto.gui_dto_models import GuiDivisionDto
from src.gui.dto.model_pipeline_services import DepartmentPipelineService, DivisionPipelineService
from src.gui.viewmodels.dialogs.base_dialog_model import BaseDialogViewModel
from src.shared.mappers.mapper_services import DepartmentMapperService, DivisionMapperService


class AddDivisionDialogModel(BaseDialogViewModel):
    close_view_with_data_signal = Signal(DivisionDomain)

    def __init__(self, division_pipeline_service: DivisionPipelineService) -> None:
        super().__init__()
        self._division_pipeline_service = division_pipeline_service

    def validate_data_dialog(self, division_data: dict[str, str]) -> None:
        division: DivisionDomain | None = None
        try:
            division = self._division_pipeline_service.process_raw_data_to_domain(division_data)
        except StructureInvalidNameError as e:
            self.error_generation_signal.emit("Некорректное наименование", f"{e}")
        except StructureExistsError as e:
            self.error_generation_signal.emit("Некорректное наименование", f"{e}")
        if division:
            self.close_view_with_data_signal.emit(division)


class EditDivisionDialogModel(AddDivisionDialogModel):
    set_view_data_signal = Signal(GuiDivisionDto)

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
        self.set_data_to_view()

    def set_data_to_view(self) -> None:
        division_dto = self._mapper.to_dialog_view_dto(self._current_division)
        self.set_view_data_signal.emit(division_dto)


class AddDepartmentDialogModel(BaseDialogViewModel):
    close_view_with_data_signal = Signal(DepartmentDomain)

    def __init__(self, department_pipeline_service: DepartmentPipelineService) -> None:
        super().__init__()
        self._pipeline_service = department_pipeline_service

    def validate_data_dialog(self, department_data: dict[str, str]) -> None:
        department: DepartmentDomain | None = None
        try:
            department = self._pipeline_service.process_raw_data_to_domain(department_data)
        except StructureInvalidNameError as e:
            self.error_generation_signal.emit("Некорректное наименование", f"{e}")
        except StructureExistsError as e:
            self.error_generation_signal.emit("Некорректное наименование", f"{e}")
        if department:
            self.close_view_with_data_signal.emit(department)


class EditDepartmentDialogModel(AddDepartmentDialogModel):
    set_view_data_signal = Signal(GuiDivisionDto)

    def __init__(
        self,
        department_pipeline_service: DepartmentPipelineService,
        department_mapper_service: DepartmentMapperService,
        current_department: DepartmentDomain,
    ) -> None:
        super().__init__(department_pipeline_service)
        self._mapper = department_mapper_service
        self._current_department = current_department

    def init_model_data(self) -> None:
        self.set_data_to_view()

    def set_data_to_view(self) -> None:
        department_dto = self._mapper.to_dialog_view_dto(self._current_department)
        self.set_view_data_signal.emit(department_dto)
