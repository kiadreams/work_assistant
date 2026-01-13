from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget


class BaseView(QWidget):
    def init_content_view(self) -> None:
        pass

    def __setup_connections(self) -> None:
        pass


class SessionWindow(BaseView):
    back_main_menu_signal = Signal()