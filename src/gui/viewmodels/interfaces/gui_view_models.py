from typing import Protocol

from PySide6.QtCore import SignalInstance

from src.core.interfaces.view_models import DivisionViewModelProtocol


class GuiDivisionViewModelProtocol(DivisionViewModelProtocol, Protocol):
    division_data_changed_signal: SignalInstance
    department_data_changed_signal: SignalInstance
