from __future__ import annotations

from typing import Protocol


class DivisionProtocol(Protocol):
    id: int
    name: str
    full_name: str | None
    employee_positions: list[EmployeePositionProtocol]

    # employee_positions: list[EmployeePosition]
    # name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    #
    # departments: Mapped[list[Department]] = relationship(
    #     back_populates="division", default_factory=list
    # )
    # employee_positions: Mapped[list[EmployeePosition]] = relationship(
    #     back_populates="division", default_factory=list
    # )
    #
    # full_name: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class DepartmentProtocol(Protocol):
    id: int


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
