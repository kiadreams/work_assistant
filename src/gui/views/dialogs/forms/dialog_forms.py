from PySide6.QtWidgets import QFormLayout, QLineEdit, QWidget


class DivisionFormWidget(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.division_name = QLineEdit()
        self.division_full_name = QLineEdit()

        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

    def get_data(self) -> dict[str, str]:
        return {"name": self.division_name.text(), "full_name": self.division_full_name.text()}

    def add_division_name_field(self, field_name: str) -> None:
        self.form_layout.addRow(field_name, self.division_name)

    def add_division_full_name_field(self, field_name: str) -> None:
        self.form_layout.addRow(field_name, self.division_full_name)
