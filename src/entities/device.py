from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    ForeignKey,
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
    from .device_location import DeviceLocation
    from .work import Work


class Device(MappedAsDataclass, Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))
    device_location_id: Mapped[int] = mapped_column(ForeignKey("device_locations.id"))

    location: Mapped[DeviceLocation] = relationship(back_populates="devices")
    works: Mapped[list[Work]] = relationship(secondary=devices_works, back_populates="devices")

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
