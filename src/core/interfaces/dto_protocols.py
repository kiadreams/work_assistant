from __future__ import annotations

import datetime
from typing import Any, Protocol


class DivisionDtoProtocol(Protocol):
    id: int | None
    name: str
    full_name: str | None
    departments: list[Any]


class DepartmentDtoProtocol(Protocol):
    id: int | None
    name: str
    division_id: int | None
    full_name: str | None


class EmployeePositionDtoProtocol(Protocol):
    id: int | None
    name: str
    number_of_position: int
    division_id: int | None
    department_id: int | None
    abbreviation: str | None
    division: DivisionDtoProtocol | None
    department: DepartmentDtoProtocol | None
    employee: EmployeeDtoProtocol | None


class EmployeeDtoProtocol(Protocol):
    id: int | None
    name: str
    last_name: str
    middle_name: str | None
    service_number: str | None
    date_of_birth: datetime.date | None
    employee_position_id: int | None
    employee_position: EmployeePositionDtoProtocol
    work_tasks: list[WorkTaskDtoProtocol]


class EquipmentDtoProtocol(Protocol):
    id: int | None
    name: str
    equipment_location_id: int | None
    inventory_number: str | None
    works: list[WorkDtoProtocol]
    location: EquipmentLocationDtoProtocol


class EquipmentLocationDtoProtocol(Protocol):
    id: int | None
    name: str
    equipment: list[EquipmentDtoProtocol]
    inventory_number: str | None


class WorkDtoProtocol(Protocol):
    id: int | None
    name: str
    year: int
    month: int | None
    work_type_id: int | None
    work_order_id: int | None
    equipment_id: int | None
    work_type: WorkTypeDtoProtocol | None
    work_order: WorkOrderDtoProtocol | None
    work_tasks: list[WorkTaskDtoProtocol]
    equipment: list[EquipmentDtoProtocol]


class WorkOrderDtoProtocol(Protocol):
    id: int | None
    number: str
    works: list[WorkDtoProtocol]


class WorkTaskDtoProtocol(Protocol):
    id: int | None
    work_id: int | None
    employee_id: int | None
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    work: WorkDtoProtocol
    employee: EmployeeDtoProtocol


class WorkTypeDtoProtocol(Protocol):
    id: int | None
    name: str
    works: list[WorkDtoProtocol]
    abbreviation: str | None
