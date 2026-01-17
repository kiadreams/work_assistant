from __future__ import annotations

from typing import Protocol


class DivisionProtocol(Protocol):
    id: int
    name: str
    full_name: str | None
    employee_positions: list[EmployeePositionProtocol]
    departments: list[DepartmentProtocol]


class DepartmentProtocol(Protocol):
    id: int
    name: str
    division_id: int | None
    full_name: str | None
    employee_positions: list[EmployeePositionProtocol]
    division: DivisionProtocol | None


class EmployeePositionProtocol(Protocol):
    id: int


class EmployeeProtocol(Protocol):
    id: int
    service_number: str | None


class EquipmentLocationProtocol(Protocol):
    id: int


class Workrotocol(Protocol):
    id: int


class WorkOrderProtocol(Protocol):
    id: int


class WorkTaskProtocol(Protocol):
    id: int


class WorkTypeProtocol(Protocol):
    id: int
