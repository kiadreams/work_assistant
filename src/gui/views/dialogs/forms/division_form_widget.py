from PySide6.QtWidgets import QFormLayout, QLineEdit, QWidget


class DivisionFormWidget(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.division_name = QLineEdit()
        self.division_full_name = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Название службы:", self.division_name)
        layout.addRow("Полное наименование службы:", self.division_full_name)
        self.setLayout(layout)

    def get_data(self) -> dict[str, str | int]:
        return {"name": self.division_name.text(), "full_name": self.division_full_name.text()}
