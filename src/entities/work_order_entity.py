from sqlalchemy import String
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from . import employee_db_tables
from . import device_db_tables
from src.databases import Base


class WorkOrder(MappedAsDataclass, Base):
    __tablename__ = 'work_orders'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    works: Mapped[list['Work']] = relationship(back_populates='work_order')

    number: Mapped[str] = mapped_column(String(20), nullable=False, default='V05110______')
