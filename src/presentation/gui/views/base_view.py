from PySide6.QtWidgets import QMessageBox, QWidget


class BaseView(QWidget):
    def init_content_view(self) -> None:
        pass

    def setup_connections(self) -> None:
        pass

    def show_warning_massage(self, title: str, message: str) -> None:
        QMessageBox.warning(self, title, message)
