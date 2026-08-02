from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt

if TYPE_CHECKING:
    from src.presentation.view_dtos import EmployeeViewDto


class EmployeeTableModel(QAbstractTableModel):
    def __init__(self) -> None:
        super().__init__()
        self._employees: list[EmployeeViewDto] = []
        self._headers = ["№\nп/п", "ФИО", "Должность", "Дата рождения"]

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:  # noqa: N802
        """Возвращает количество строк (элементов в списке ViewModel)."""
        return len(self._employees)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:  # noqa: N802
        # У нас строго 3 колонки
        return len(self._headers)

    def data(
        self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.ItemDataRole.DisplayRole
    ) -> str | None:
        """Предоставляет данные для каждой ячейки."""
        if not index.isValid() or not (0 <= index.row() < len(self._employees)):
            return None
        emp_dto = self._employees[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            match index.column():
                case 0:
                    return str(index.row() + 1)
                case 1:
                    return f"{emp_dto.last_name} {emp_dto.name} {emp_dto.middle_name}"
                case 2:
                    return emp_dto.employee_position
                case 3:
                    if emp_dto.date_of_birth:
                        return emp_dto.date_of_birth.strftime("%d.%m.%Y")
                    return ""
        return None

    def headerData(  # noqa: N802
        self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole
    ) -> str | None:
        """Предоставляет данные для заголовков."""
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        return None

    def set_employees(self, employees: list[EmployeeViewDto]) -> None:
        """Safety update employee data of table."""
        self.beginResetModel()  # Уведомляем QTableView, что данные сейчас полностью изменятся
        self._employees = employees
        self.endResetModel()  # Таблица мгновенно перерисовывается

    def get_employee_by_row(self, row: int) -> EmployeeViewDto | None:
        """Позволяет View мгновенно забрать DTO выбранной строки."""
        if 0 <= row < len(self._employees):
            return self._employees[row]
        return None
