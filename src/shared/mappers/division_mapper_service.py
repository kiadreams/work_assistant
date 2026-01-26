from src.core.models.division_domain import DivisionDomain
from src.gui.dto.gui_dto_models import GuiDivisionDto


class DivisionMapperService:
    def get_gui_division_dto(self, division: DivisionDomain) -> GuiDivisionDto:
        gui_division_dto = GuiDivisionDto.model_validate(division)
        return gui_division_dto
