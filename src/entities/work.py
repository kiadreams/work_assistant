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
from .associations.equipment_work import equipment_works


if TYPE_CHECKING:
    from .work_type import WorkType
    from .work_order import WorkOrder
    from .work_task import WorkTask
    from .equipment import Equipment


class Work(MappedAsDataclass, Base):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    work_type: Mapped[WorkType] = relationship(back_populates="works")
    work_order: Mapped[WorkOrder] = relationship(back_populates="works")
    work_tasks: Mapped[list[WorkTask]] = relationship(back_populates="work")
    equipment: Mapped[list[Equipment]] = relationship(
        secondary=equipment_works, back_populates="works"
    )

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
    equipment_id: Mapped[int | None] = mapped_column(
        ForeignKey("equipment.id"), nullable=True, default=None
    )
