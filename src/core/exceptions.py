class BusinessLogicError(Exception):
    """Базовый класс для всех ошибок бизнес-логики приложения."""

    pass


class StructureError(BusinessLogicError):
    """Базовый класс для всех ошибок, связанных с сущностью 'Подразделение'."""

    pass


class StructureExistsError(StructureError):
    """Служба с таким наименованием уже существует."""

    pass


class StructureNotFoundError(StructureError):
    """Служба не найдена."""

    pass


class StructureInvalidNameError(StructureError):
    """Некорректное имя подразделения."""

    pass
