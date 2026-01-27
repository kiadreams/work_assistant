from __future__ import annotations

from typing import Any


class DepartmentDomain:
    def __init__(
        self,
        *,
        department_id: int | None = None,
        name: str,
        full_name: str | None = None,
        division_id: int | None = None,
    ) -> None:
        self.id = department_id
        self.name = name
        self.full_name = full_name
        self.division_id = division_id

    @property
    def model_data(self) -> dict[str, Any]:
        return vars(self)
