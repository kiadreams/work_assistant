from sqlalchemy import Column, ForeignKey, Table

from src.database import db_manager

equipment_works = Table(
    "equipment_works",  # Имя промежуточной таблицы
    db_manager.Base.metadata,  # Привязка к метаданным Base
    # Колонка, ссылающаяся на первичный ключ таблицы list_of_works.id
    Column("work_id", ForeignKey("works.id"), primary_key=True),
    # Колонка, ссылающаяся на первичный ключ таблицы devices.id
    Column("equipment_id", ForeignKey("equipment.id"), primary_key=True),
)
