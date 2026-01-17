from __future__ import annotations

import datetime
from typing import Protocol

from database.entities import WorkType


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
    name: str
    division_id: int | None
    department_id: int | None
    abbreviation: str | None
    number_of_position: int
    division: DivisionProtocol | None
    department: DepartmentProtocol | None
    employee: EmployeeProtocol | None


class EmployeeProtocol(Protocol):
    id: int
    name: str
    last_name: str
    middle_name: str | None
    service_number: str | None
    date_of_birth: datetime.date | None
    employee_position_id: int
    employee_position: EmployeePositionProtocol
    work_tasks: list[WorkTaskProtocol]


class EquipmentProtocol(Protocol):
    id: int
    name: str
    equipment_location_id: int
    inventory_number: str | None
    works: list[WorkProtocol]
    location: EquipmentLocationProtocol


class EquipmentLocationProtocol(Protocol):
    id: int
    name: str
    equipment: list[EquipmentProtocol]
    inventory_number: str | None


class WorkProtocol(Protocol):
    id: int
    name: str
    year: int
    month: int | None
    work_type_id: int | None
    work_order_id: int | None
    equipment_id: int | None
    work_type: WorkType | None
    work_order: WorkProtocol | None
    work_tasks: list[WorkTaskProtocol]
    equipment: list[EquipmentProtocol]


class WorkOrderProtocol(Protocol):
    id: int
    number: str
    works: list[WorkProtocol]


class WorkTaskProtocol(Protocol):
    id: int
    work_id: int
    employee_id: int
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    work: WorkProtocol
    employee: EmployeeProtocol


class WorkTypeProtocol(Protocol):
    id: int
    name: str
    works: list[WorkProtocol]
    abbreviation: str | None
