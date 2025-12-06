from dataclasses import dataclass

from sqlalchemy import String
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column
from src.packages.databases.engin_db import Base


@dataclass
class Device(MappedAsDataclass, Base):
    __tablename__ = 'devices'

    inventory_number: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    installation_location: Mapped[str] = mapped_column(String(50))
