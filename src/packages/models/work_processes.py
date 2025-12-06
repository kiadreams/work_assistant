from dataclasses import dataclass
from datetime import datetime

from src.packages.models.work import Work
from src.packages.models.employees import Employee


@dataclass
class EmployeeEvent:
    work: Work
    employee: Employee
    start_date: datetime
    end_date: datetime

