from PySide6.QtCore import QAbstractTableModel, QModelIndex, QObject, QPersistentModelIndex, Qt

from src.gui.viewmodels.interfaces.gui_view_models import GuiDivisionViewModelProtocol


class DivisionReportDivisionTableModel(QAbstractTableModel):
    def __init__(self, viewmodel: GuiDivisionViewModelProtocol, parent: QObject | None = None):
        super().__init__(parent)
        self.vm = viewmodel
        self.headers = ["№\nп/п", "Служба", "Полное наименование"]
        self.attributes = ["", "name", "full_name"]
        self.vm.division_data_changed_signal.connect(self.layoutChanged.emit)

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        """Возвращает количество строк (элементов в списке ViewModel)."""
        return len(self.vm.divisions)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        """Возвращает количество столбцов (заголовков)."""
        return len(self.headers)

    def data(
        self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.ItemDataRole.DisplayRole
    ) -> str | None:
        """Предоставляет данные для каждой ячейки."""
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            if col == 0:
                return str(row + 1)
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


class DivisionReportDepartmentTableModel(QAbstractTableModel):
    def __init__(self, viewmodel: GuiDivisionViewModelProtocol, parent: QObject | None = None):
        super().__init__(parent)
        self.vm = viewmodel
        self.headers = ["№\nп/п", "Подразделение\n(отдел)", "Полное наименование подразделения"]
        self.attributes = ["", "name", "full_name"]
        self.vm.department_data_changed_signal.connect(self.layoutChanged.emit)

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        """Возвращает количество строк (элементов в списке ViewModel)."""
        return len(self.vm.departments)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        """Возвращает количество столбцов (заголовков)."""
        return len(self.headers)

    def data(
        self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.ItemDataRole.DisplayRole
    ) -> str | None:
        """Предоставляет данные для каждой ячейки."""
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            if col == 0:
                return str(row + 1)
            # Безопасный доступ к данным из списка объектов Division
            if row < len(self.vm.departments):
                department = self.vm.departments[row]
                attribute_name = self.attributes[col]
                value = getattr(department, attribute_name)
                return str(value)
        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole
    ) -> str | None:
        """Предоставляет данные для заголовков."""
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.headers[section]
        return None
