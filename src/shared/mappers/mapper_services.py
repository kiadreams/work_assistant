from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain
from src.gui.dto.gui_dto_models import GuiDepartmentDto, GuiDivisionDto


class DivisionMapperService:
    @staticmethod
    def to_dialog_view_dto(division: DivisionDomain) -> GuiDivisionDto:
        gui_division_dto = GuiDivisionDto(name=division.name, full_name=division.full_name)
        return gui_division_dto


class DepartmentMapperService:
    @staticmethod
    def to_dialog_view_dto(department: DepartmentDomain) -> GuiDepartmentDto:
        gui_department_dto = GuiDepartmentDto(name=department.name, full_name=department.full_name)
        return gui_department_dto
