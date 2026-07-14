class ApplicationError(Exception):
    """Базовый класс всех исключений в приложении."""

    pass


class BusinessLogicError(ApplicationError):
    """Базовый класс для всех ошибок бизнес-логики приложения."""

    pass


class ViewFormError(ApplicationError):
    """Базовый класс для всех ошибок связанных с интерфейсом."""

    pass
