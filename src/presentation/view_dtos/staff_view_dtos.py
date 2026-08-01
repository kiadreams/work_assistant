from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CompanyViewDto:
    id: int
    name: str
    full_name: str


@dataclass(frozen=True)
class DivisionViewDto:
    id: int
    name: str
    full_name: str
    company_id: int


@dataclass(frozen=True)
class DepartmentViewDto:
    id: int
    name: str
    full_name: str
    division_id: int


@dataclass(frozen=True)
class EmployeeViewDto:
    id: int
    name: str
    last_name: str
    middle_name: str
    employee_position: str
    employee_position_id: int
    service_number: str
    date_of_birth: date
