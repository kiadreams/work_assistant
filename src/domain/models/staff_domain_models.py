from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(kw_only=True)
class CompanyDomain:
    id: int
    name: str
    full_name: str | None


@dataclass(kw_only=True)
class DivisionDomain:
    id: int
    name: str
    full_name: str | None
    company_id: int



@dataclass(kw_only=True)
class DepartmentDomain:
    id: int
    name: str
    full_name: str | None
    division_id: int


@dataclass(kw_only=True)
class EmployeeDomain:
    id: int
    name: str
    last_name: str
    middle_name: str
    employee_position: str
    employee_position_id: int
    service_number: str | None
    date_of_birth: date | None

