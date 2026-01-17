from __future__ import annotations


class DepartmentDomain:
    def __init__(
        self, department_id: int, name: str | None, division_id: int, full_name: str | None = None
    ) -> None:
        self._id = department_id
        self._name = name
        self._division_id = division_id
        self._full_name = full_name

    def model_validate(self) -> None:
        pass
