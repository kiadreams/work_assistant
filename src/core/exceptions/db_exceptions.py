from __future__ import annotations

from typing import Any

from src.core.exceptions.base_exceptions import ApplicationError
from src.core.models.department_domain import DepartmentDomain
from src.core.models.division_domain import DivisionDomain


class EntityTypeError(ApplicationError):
    """Исключение выбрасывается, когда вместо сущности передаётся None."""

    def __init__(self, entity_type: type, expected_type: type):
        self.entity_type = entity_type
        self.expected_type = expected_type
        super().__init__(f"Ожидался тип f{self.expected_type} а передан f{self.entity_type}.")


class EntityNotFoundError(ApplicationError):
    """Исключение выбрасывается, когда сущность не найдена в базе данных."""

    def __init__(self, entity_id: int, entity_name: str = "Entity"):
        self.entity_id = entity_id
        self.entity_name = entity_name
        super().__init__(f"{entity_name} с ID={entity_id} не найдена.")


class EntityAttributeTypeError(ApplicationError):
    """Исключение выбрасывается, когда у атрибута сущности неправильный тип или значение None."""

    def __init__(self, attr_name: str, attr_type: type, expected_type: type):
        self.attr_name = attr_name
        self.attr_type = attr_type
        self.expected_type = expected_type
        super().__init__(
            f"У атрибута {self.attr_name} ожидался тип {self.expected_type} а передан {self.attr_type}."
        )


class DivisionTypeError(EntityTypeError):
    """Исключение выбрасывается, когда вместо DivisionDomain передаётся другой тип или None."""

    def __init__(self, entity: Any):
        super().__init__(entity_type=type(entity), expected_type=type(DivisionDomain))


class DepartmentTypeError(EntityTypeError):
    """Исключение выбрасывается, когда вместо DepartmentDomain передаётся другой тип или None."""

    def __init__(self, entity: Any):
        super().__init__(entity_type=type(entity), expected_type=type(DepartmentDomain))


class DivisionNotFoundError(EntityNotFoundError):
    """Специфическое исключение для службы."""

    def __init__(self, division_id: int):
        super().__init__(division_id, entity_name="Division")


# Если вы редактируете сотрудника
class DepartmentNotFoundError(EntityNotFoundError):
    """Специфическое исключение для отдела."""

    def __init__(self, department_id: int):
        super().__init__(department_id, entity_name="Department")
