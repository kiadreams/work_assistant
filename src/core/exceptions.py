class BusinessLogicError(Exception):
    """Базовый класс для всех ошибок бизнес-логики приложения."""

    pass


class DivisionError(BusinessLogicError):
    """Базовый класс для всех ошибок, связанных с сущностью 'Подразделение'."""

    pass


class DivisionExistsError(DivisionError):
    """Служба с таким наименованием уже существует."""

    pass


class DivisionNotFoundError(DivisionError):
    """Служба не найдена."""

    pass


class DivisionInvalidNameError(DivisionError):
    """Некорректное имя подразделения."""

    pass
