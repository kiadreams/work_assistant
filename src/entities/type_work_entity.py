from sqlalchemy import String
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from . import employee_db_tables
from . import device_db_tables
from src.databases import Base
from . import association_db_tables


class WorkType(MappedAsDataclass, Base):
    __tablename__ = 'work_types'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    works: Mapped[list['Work']] = relationship(back_populates='type_of_maintenance')

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)