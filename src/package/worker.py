from dataclasses import dataclass
from datetime import date


@dataclass
class Worker:
    name: str
    last_name: str
    middle_name: str
    date_of_birth: date
    post: str
