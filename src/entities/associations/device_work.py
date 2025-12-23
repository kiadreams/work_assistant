from sqlalchemy import Table, Column, ForeignKey

from src.databases import database

devices_in_works = Table(
    "devices_in_works",  # Имя промежуточной таблицы
    database.Base.metadata,  # Привязка к метаданным Base
    # Колонка, ссылающаяся на первичный ключ таблицы list_of_works.id
    Column("work_id", ForeignKey('list_of_works.id'), primary_key=True),
    # Колонка, ссылающаяся на первичный ключ таблицы devices.id
    Column("device_id", ForeignKey('devices.id'), primary_key=True),
)