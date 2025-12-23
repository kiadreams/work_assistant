from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from src.databases import Base
from . import work_db_tables


class EmployeePosition(MappedAsDataclass, Base):
    __tablename__ = 'employee_positions'

    __table_args__ = (
        CheckConstraint(
            sqltext='(service_id IS NOT NULL AND department_id IS NULL) '
                    'OR (service_id IS NULL AND department_id IS NOT NULL)',
            name='chk_single_department'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))
    department_id: Mapped[int] = mapped_column(ForeignKey('departments.id'))

    service: Mapped['Service'] = relationship(back_populates='employee_positions', default=None)
    department: Mapped['Department'] = relationship(back_populates='employee_positions', default=None)
    employees: Mapped[list['Employee']] = relationship(back_populates='employee_position', default_factory=list)

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)