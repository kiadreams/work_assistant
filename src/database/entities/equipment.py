from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

from src.database.db_manager import Base

from .associations.equipment_work import equipment_works

if TYPE_CHECKING:
    from .equipment_location import EquipmentLocation
    from .work import Work


class Equipment(MappedAsDataclass, Base):
    __tablename__ = "equipment"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))
    equipment_location_id: Mapped[int] = mapped_column(ForeignKey("equipment_locations.id"))

    location: Mapped[EquipmentLocation] = relationship(back_populates="equipment")
    works: Mapped[list[Work]] = relationship(secondary=equipment_works, back_populates="equipment")

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
