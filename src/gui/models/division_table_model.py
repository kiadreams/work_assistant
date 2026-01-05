from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from src.viewmodels.qt_interfaces import QtDivisionVMProtocol


class DivisionTableModel(QAbstractTableModel):
    def __init__(self, viewmodel: QtDivisionVMProtocol, parent=None):
        super().__init__(parent)
        self.vm = viewmodel
        self.headers = ["Служба", "Полное наименование"]
        self.attributes = ["name", "full_name"]

        self.vm.data_changed_signal.connect(self.layoutChanged.emit)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """Возвращает количество строк (элементов в списке ViewModel)."""
        return len(self.vm.divisions)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """Возвращает количество столбцов (заголовков)."""
        return len(self.headers)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> str | None:
        """Предоставляет данные для каждой ячейки."""
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            # Безопасный доступ к данным из списка объектов Division
            if row < len(self.vm.divisions):
                division = self.vm.divisions[row]
                attribute_name = self.attributes[col]
                value = getattr(division, attribute_name)
                return str(value)
        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole
    ) -> str | None:
        """Предоставляет данные для заголовков."""
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.headers[section]
        return None
