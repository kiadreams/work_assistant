from __future__ import annotations

from core.models.department_domain import DepartmentDomain


class DivisionDomain:
    id: int
    name: str
    full_name: str | None
    departments: list[DepartmentDomain] = []
