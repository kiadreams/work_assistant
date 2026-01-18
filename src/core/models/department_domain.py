from __future__ import annotations

from core.interfaces.data_protocols import DepartmentDataProtocol


class DepartmentDomain:
    def __init__(
        self,
        *,
        name: str,
        division_id: int | None = None,
        full_name: str | None = None,
        department_id: int | None = None,
    ) -> None:
        self._id = department_id
        self._name = name
        self._division_id = division_id
        self._full_name = full_name

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def division_id(self) -> int | None:
        return self._division_id

    @property
    def full_name(self) -> str | None:
        return self._full_name

    @classmethod
    def model_validate(cls, department_data: DepartmentDataProtocol) -> DepartmentDomain:
        return cls(
            name=department_data.name,
            department_id=department_data.id,
            division_id=department_data.division_id,
            full_name=department_data.full_name,
        )
