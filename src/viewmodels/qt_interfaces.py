from typing import Protocol

from PySide6.QtCore import Signal

from src.core.interfaces.viewmodels import DivisionViewModelProtocol


class QtBaseVMProtocol(DivisionViewModelProtocol, Protocol):
    data_changed_signal: Signal


class QtDivisionVMProtocol(QtBaseVMProtocol, Protocol):
    pass
