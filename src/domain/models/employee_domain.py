from __future__ import annotations


class EmployeeDomain:
    def __init__(
        self,
        *,
        employee_id: int,
        name: str,
        last_name: str,
        employee_position: str,
        employee_position_id: int,
        service_number: str | None,
    ) -> None:
        self.id = employee_id
        self.name = name
        self.last_name = last_name
        self.employee_position = employee_position
        self.employee_position_id = employee_position_id
        self.service_number = service_number
        self.work_tasks = []
