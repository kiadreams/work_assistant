from sqlalchemy import String, ForeignKey, SmallInteger, extract, func
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from . import employee_db_tables
from . import device_db_tables
from src.databases import Base
from . import association_db_tables


class Work(MappedAsDataclass, Base):
    __tablename__ = 'works'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    type_of_maintenance: Mapped['TypeOfMaintenance'] = relationship(back_populates='works')
    work_order: Mapped['WorkOrder'] = relationship(back_populates='works')
    events: Mapped['WorkEvent'] = relationship(back_populates='work')
    devices: Mapped[list['device_db_tables.Device']] = relationship(secondary=association_db_tables.devices_in_works,
                                                           back_populates='works')

    year: Mapped[int] = mapped_column(SmallInteger,
                                      nullable=False,
                                      server_default=extract('year', func.now()))
    month: Mapped[int | None] = mapped_column(SmallInteger, nullable=True, default=None)
    work_type_id: Mapped[int | None] = mapped_column(ForeignKey('work_types.id'), nullable=True, default=None)
    work_order_id: Mapped[int | None] = mapped_column(ForeignKey('work_orders.id'), nullable=True, default=None)
    device_id: Mapped[int | None] = mapped_column(ForeignKey('devices.id'), nullable=True, default=None)