from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models import CompanyDomain, DepartmentDomain, DivisionDomain, EmployeeDomain


@dataclass(frozen=True, kw_only=True)
class CompanyViewDto:
    display_name: str
    id: int
    name: str

    @classmethod
    def from_domain(cls, domain: CompanyDomain) -> CompanyViewDto:
        """Фабричный метод, создающий View DTO на основе Доменной Модели."""
        display_text = domain.full_name or domain.name
        return cls(id=domain.id, display_name=display_text, name=domain.name)


@dataclass(frozen=True, kw_only=True)
class DivisionViewDto:
    display_name: str
    id: int
    name: str
    company_id: int

    @classmethod
    def from_domain(cls, domain: DivisionDomain) -> DivisionViewDto:
        """Фабричный метод, создающий View DTO на основе Доменной Модели."""
        display_text = domain.full_name or domain.name
        return cls(
            id=domain.id, display_name=display_text, name=domain.name, company_id=domain.company_id
        )


@dataclass(frozen=True, kw_only=True)
class DepartmentViewDto:
    display_name: str
    id: int
    name: str
    division_id: int

    @classmethod
    def from_domain(cls, domain: DepartmentDomain) -> DepartmentViewDto:
        """Фабричный метод, создающий View DTO на основе Доменной Модели."""
        display_text = domain.full_name or domain.name
        return cls(
            id=domain.id,
            display_name=display_text,
            name=domain.name,
            division_id=domain.division_id,
        )


@dataclass(frozen=True, kw_only=True)
class EmployeeViewDto:
    display_name: str
    id: int
    name: str
    last_name: str
    middle_name: str
    employee_position: str
    employee_position_id: int
    service_number: str | None
    date_of_birth: date | None

    @classmethod
    def from_domain(cls, domain: EmployeeDomain) -> EmployeeViewDto:
        """Фабричный метод, создающий View DTO на основе Доменной Модели."""
        display_text = f"{domain.last_name} {domain.name} {domain.middle_name}"
        return cls(
            id=domain.id,
            display_name=display_text,
            name=domain.name,
            last_name=domain.last_name,
            middle_name=domain.middle_name,
            employee_position=domain.employee_position,
            employee_position_id=domain.employee_position_id,
            service_number=domain.service_number,
            date_of_birth=domain.date_of_birth,
        )
