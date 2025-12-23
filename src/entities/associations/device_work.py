from sqlalchemy import Table, Column, ForeignKey

from src.databases import database

devices_works = Table(
    'devices_works',  # Имя промежуточной таблицы
    database.Base.metadata,  # Привязка к метаданным Base
    # Колонка, ссылающаяся на первичный ключ таблицы list_of_works.id
    Column('work_id', ForeignKey('works.id'), primary_key=True),
    # Колонка, ссылающаяся на первичный ключ таблицы devices.id
    Column('device_id', ForeignKey('devices.id'), primary_key=True),
)