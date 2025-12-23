from sqlalchemy import String
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from src.databases.database import Base
from . import association_db_tables
from . import work_db_tables


class DeviceLocation(MappedAsDataclass, Base):
    __tablename__ = 'device_locations'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))

    devices: Mapped[list['Device']] = relationship(back_populates='location')

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
