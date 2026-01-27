from typing import Any

from PySide6.QtCore import QObject, Signal


class BaseViewModel(QObject):
    close_view_with_data_signal = Signal(Any)
    error_generation_signal = Signal(str, str)
    set_view_data_signal = Signal(Any)

    def init_model_data(self) -> None:
        pass
