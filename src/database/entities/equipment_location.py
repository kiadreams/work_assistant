from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

from src.database.db_manager import Base

if TYPE_CHECKING:
    from .equipment import Equipment


class EquipmentLocation(MappedAsDataclass, Base):
    __tablename__ = "equipment_locations"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))

    equipment: Mapped[list[Equipment]] = relationship(back_populates="location")

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
