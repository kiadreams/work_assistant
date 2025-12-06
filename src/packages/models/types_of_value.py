import enum


class TypeOfWork(enum.StrEnum):
    SETTING_UP = 'наладка'
    FIRST_CONTROL = 'первый профилактический контроль'
    RESTORATION = 'восстановление'
    CONTROL = 'профилактический контроль'
    TESTING = 'опробование'
    TESTING_CONTROL = 'тестовый контроль'


class EmployeePosition(enum.StrEnum):
    ENGINEER = 'инженер'
    ENGINEER_2_CATEGORY = 'инженер 2-ой категории'
    ENGINEER_1_CATEGORY = 'инженер 1-ой категории'
    LEAD_ENGINEER = 'ведущий инженер'
    LEADING_SPECIALIST = 'ведущий специалист'
