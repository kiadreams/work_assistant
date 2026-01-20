from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import ValidationError
from PySide6.QtCore import QObject, Signal

from core.models.division_domain import DivisionDomain
from gui.dto.models import DivisionDto

if TYPE_CHECKING:
    from core.interfaces.validators import DivisionValidatorProtocol


class AddDivisionDialogModel(QObject):
    close_dialog_signal = Signal()
    show_error_signal = Signal()

    def __init__(self, division_validator: DivisionValidatorProtocol):
        super().__init__()
        self._division_validator = division_validator
        self._new_division: DivisionDomain | None = None

    def handle_ok_button_pressed(self, division_data: dict[str, str]) -> None:
        try:
            division_dto = DivisionDto.model_validate(division_data)
        except ValidationError as e:
            self.show_error_signal.emit(f"Ошибка формата: {e.errors()[0]['msg']}")
            return
        division = DivisionDomain.division_from_data(division_dto)
        if self._division_validator.is_valid_division(division):
            self.close_dialog_signal.emit(True)
        else:
            self.show_error_signal.emit("Служба с таким наименованием уже существует.")

    @property
    def division(self) -> DivisionDomain | None:
        return self._new_division

    def teardown(self) -> None:
        """Очистка всех внутренних ресурсов сессии."""
        for coordinator in self._view_coordinators.values():
            if hasattr(coordinator, "teardown"):
                coordinator.teardown()
