from dataclasses import dataclass
from datetime import timedelta

from src.packages.models.device import Device
from src.packages.models.types_of_value import TypeOfWork


@dataclass
class Work:
    name: str
    device: Device
    type_of_work: TypeOfWork


@dataclass
class WorkOrder:
    numbers: int
    dedicated_hours: timedelta
