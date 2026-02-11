from typing import Any


class EntityNotFoundError(Exception):
    """Исключение выбрасывается, когда сущность не найдена в базе данных."""

    def __init__(self, entity_id: int, entity_name: str = "Entity"):
        self.entity_id = entity_id
        self.entity_name = entity_name
        super().__init__(f"{entity_name} с ID={entity_id} не найдена.")


class AttributeOfEntityNotFoundError(Exception):
    """Исключение выбрасывается, когда атрибут сущность или отсутствует или None."""

    def __init__(self, attr_name: str, attr_value: Any, entity_name: str = "Entity"):
        self.attr_name = attr_name
        self.attr_value = attr_value
        self.entity_name = entity_name
        super().__init__(
            f'У {self.entity_name} отсутствует атрибут "{self.entity_name}": {self.attr_value}.'
        )


class DivisionNotFoundError(EntityNotFoundError):
    """Специфическое исключение для службы."""

    def __init__(self, division_id: int | None):
        super().__init__(division_id, entity_name="Division")


# Если вы редактируете сотрудника
class DepartmentNotFoundError(EntityNotFoundError):
    """Специфическое исключение для отдела."""

    def __init__(self, department_id: int | None):
        super().__init__(department_id, entity_name="Department")
