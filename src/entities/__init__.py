# src/entities/__init__.py

from .deprtment_entity import Department
from .device_entity import Device
from .device_location_entity import DeviceLocation
from .employee_entity import Employee
from .employee_position_entity import EmployeePosition
from .service_entity import Service
from .type_work_entity import WorkType
from .work_entity import Work
from .work_event_entity import WorkEvent
from .work_order_entity import WorkOrder


# Опционально: Импортировать базовый класс, если он лежит здесь
# from .base import Base