from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from src.databases import Base
from . import association_db_tables
from . import work_db_tables


class Device(MappedAsDataclass, Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))
    device_location_id: Mapped[int] = mapped_column(ForeignKey('device_locations.id'))

    location: Mapped['DeviceLocation'] = relationship(back_populates='devices')
    works: Mapped[list['work_db_tables.Work']] = relationship(secondary=association_db_tables.devices_in_works,
                                                     back_populates='devices')

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
