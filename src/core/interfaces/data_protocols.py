from __future__ import annotations

import datetime
from typing import Protocol


class DivisionDataProtocol(Protocol):
    id: int | None
    name: str
    full_name: str | None
    departments: list[DepartmentDataProtocol]


class DepartmentDataProtocol(Protocol):
    id: int | None
    name: str
    division_id: int | None
    full_name: str | None


class EmployeePositionDataProtocol(Protocol):
    id: int | None
    name: str
    number_of_position: int
    division_id: int | None
    department_id: int | None
    abbreviation: str | None
    division: DivisionDataProtocol | None
    department: DepartmentDataProtocol | None
    employee: EmployeeDataProtocol | None


class EmployeeDataProtocol(Protocol):
    id: int | None
    name: str
    last_name: str
    middle_name: str | None
    service_number: str | None
    date_of_birth: datetime.date | None
    employee_position_id: int | None
    employee_position: EmployeePositionDataProtocol
    work_tasks: list[WorkTaskDataProtocol]


class EquipmentDataProtocol(Protocol):
    id: int | None
    name: str
    equipment_location_id: int | None
    inventory_number: str | None
    works: list[WorkDataProtocol]
    location: EquipmentLocationDataProtocol


class EquipmentLocationDataProtocol(Protocol):
    id: int | None
    name: str
    equipment: list[EquipmentDataProtocol]
    inventory_number: str | None


class WorkDataProtocol(Protocol):
    id: int | None
    name: str
    year: int
    month: int | None
    work_type_id: int | None
    work_order_id: int | None
    equipment_id: int | None
    work_type: WorkTypeDataProtocol | None
    work_order: WorkOrderDataProtocol | None
    work_tasks: list[WorkTaskDataProtocol]
    equipment: list[EquipmentDataProtocol]


class WorkOrderDataProtocol(Protocol):
    id: int | None
    number: str
    works: list[WorkDataProtocol]


class WorkTaskDataProtocol(Protocol):
    id: int | None
    work_id: int | None
    employee_id: int | None
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    work: WorkDataProtocol
    employee: EmployeeDataProtocol


class WorkTypeDataProtocol(Protocol):
    id: int | None
    name: str
    works: list[WorkDataProtocol]
    abbreviation: str | None
