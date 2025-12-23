from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from src.databases import Base
from . import work_db_tables


class Department(MappedAsDataclass, Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))

    service: Mapped['Service'] = relationship(back_populates='departments')
    employee_positions: Mapped[list['EmployeePosition']] = relationship(
        back_populates='department',
        default_factory=list
    )
    full_name: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)