from typing import Any

from src.gui.viewmodels.base_view_model import BaseViewModel


class BaseDialogViewModel(BaseViewModel):
    def init_model_data(self) -> None:
        pass

    def set_data_to_view(self) -> None:
        pass

    def validate_data_dialog(self, structure_data: dict[Any, Any]) -> None:
        pass
