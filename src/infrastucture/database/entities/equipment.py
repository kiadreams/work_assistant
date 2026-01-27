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

from src.infrastucture.database.db_manager import Base

from .associations.equipment_work import equipment_works

if TYPE_CHECKING:
    from .equipment_location import EquipmentLocation
    from .work import Work


class Equipment(MappedAsDataclass, Base):
    __tablename__ = "equipment"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    equipment_location_id: Mapped[int] = mapped_column(
        ForeignKey("equipment_locations.id"), nullable=False
    )

    location: Mapped[EquipmentLocation] = relationship(back_populates="equipment", init=False)
    works: Mapped[list[Work]] = relationship(
        secondary=equipment_works, back_populates="equipment", default_factory=list
    )

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
