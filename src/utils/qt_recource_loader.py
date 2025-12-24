from PySide6.QtCore import QFile, QIODevice, QTextStream, QStringConverter

from src.constants import QtResources, QtStyleResources


class ResourceLoader:
    def __init__(self, resource: QtResources) -> None:
        self.resource = resource
        self.__qfile = QFile(self.resource)

    def load_style(self) -> str:
        if not isinstance(self.resource, QtStyleResources):
            raise TypeError(
                f"Неверный тип ресурса, ожидался тип QtStyleResources, а передали {type(self.resource)}"
            )
        if self.__check_qfile():
            stream = QTextStream(self.__qfile)
            stream.setEncoding(QStringConverter.Encoding.Utf8)
            stylesheet = stream.readAll()
            self.__qfile.close()
            return stylesheet
        else:
            return ""

    def __check_qfile(self) -> bool:
        if not self.__qfile.open(QIODevice.OpenModeFlag.ReadOnly):
            print(f"Ошибка: Не удалось открыть QSS файл из ресурса по адресу {self.resource}")
            return False
        return True
