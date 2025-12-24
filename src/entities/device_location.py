from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import (
    MappedAsDataclass,
    Mapped,
    mapped_column,
    relationship,
)

from ..databases.database import Base


if TYPE_CHECKING:
    from .device import Device


class DeviceLocation(MappedAsDataclass, Base):
    __tablename__ = "device_locations"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))

    devices: Mapped[list[Device]] = relationship(back_populates="location")

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
