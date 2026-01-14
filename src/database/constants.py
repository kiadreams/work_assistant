from enum import StrEnum


class DbTables(StrEnum):
    DIVISIONS = "divisions"
    DEPARTMENTS = "departments"
    EMPLOYEE_POSITIONS = "employee_positions"
    EMPLOYEES = "employees"
    EQUIPMENT_LOCATIONS = "equipment_locations"
    EQUIPMENTS = "equipment"
    WORK_TYPES = "work_types"
    WORKS = "works"
    WORK_TASKS = "work_tasks"
    WORK_ORDERS = "work_orders"
