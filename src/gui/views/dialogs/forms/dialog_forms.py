from PySide6.QtWidgets import QFormLayout, QLineEdit, QWidget


class StructureFormWidget(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.structure_name = QLineEdit()
        self.structure_full_name = QLineEdit()

        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

    def get_data(self) -> dict[str, str]:
        return {"name": self.structure_name.text(), "full_name": self.structure_full_name.text()}

    def add_structure_name_field(self, field_name: str) -> None:
        self.form_layout.addRow(field_name, self.structure_name)

    def add_structure_full_name_field(self, field_name: str) -> None:
        self.form_layout.addRow(field_name, self.structure_full_name)
