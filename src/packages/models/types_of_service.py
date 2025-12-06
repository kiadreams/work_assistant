import datetime
from dataclasses import dataclass

from sqlalchemy import String, SmallInteger
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column

from src.packages.databases.engin_db import Base


@dataclass
class TypesOfService(MappedAsDataclass, Base):
    __tablename__ = 'types_of_service'

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, init=False, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    abbreviation: Mapped[str] = mapped_column(String(20), nullable=False)