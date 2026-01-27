class EntityNotFoundError(Exception):
    """Исключение выбрасывается, когда сущность не найдена в базе данных."""

    def __init__(self, entity_id: int, entity_name: str = "Entity"):
        self.entity_id = entity_id
        self.entity_name = entity_name
        super().__init__(f"{entity_name} с ID={entity_id} не найдена.")


class DivisionNotFoundError(EntityNotFoundError):
    """Специфическое исключение для службы."""

    def __init__(self, division_id: int):
        super().__init__(division_id, entity_name="Division")


# Если вы редактируете сотрудника
class DepartmentNotFoundError(EntityNotFoundError):
    """Специфическое исключение для отдела."""

    def __init__(self, department_id: int):
        super().__init__(department_id, entity_name="Department")
