from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    ForeignKey,
    SmallInteger,
    extract,
    func,
)
from sqlalchemy.orm import (
    MappedAsDataclass,
    Mapped,
    mapped_column,
    relationship,
)

from ..databases.database import Base
from .associations.device_work import devices_works


if TYPE_CHECKING:
    from .work_type import WorkType
    from .work_order import WorkOrder
    from .work_event import WorkEvent
    from .device import Device


class Work(MappedAsDataclass, Base):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    work_type: Mapped[WorkType] = relationship(back_populates="works")
    work_order: Mapped[WorkOrder] = relationship(back_populates="works")
    events: Mapped[WorkEvent] = relationship(back_populates="work")
    devices: Mapped[list[Device]] = relationship(secondary=devices_works, back_populates="works")

    year: Mapped[int] = mapped_column(
        SmallInteger, nullable=False, server_default=extract("year", func.now())
    )
    month: Mapped[int | None] = mapped_column(SmallInteger, nullable=True, default=None)
    work_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("work_types.id"), nullable=True, default=None
    )
    work_order_id: Mapped[int | None] = mapped_column(
        ForeignKey("work_orders.id"), nullable=True, default=None
    )
    device_id: Mapped[int | None] = mapped_column(
        ForeignKey("devices.id"), nullable=True, default=None
    )
