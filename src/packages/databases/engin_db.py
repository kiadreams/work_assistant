from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


DATABASE_URL = 'sqlite:///src/packages/databases/work_database.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def create_db_tables():
    print(f"Подключение к базе данных {engine.url} и создание таблиц...")

    # --- ЭТА КОМАНДА СОЗДАЕТ ТАБЛИЦЫ ---
    # Она проверяет все импортированные классы, наследуемые от Base,
    # и создает таблицы, если они еще не существуют.
    Base.metadata.create_all(engine)

    print("Таблицы успешно созданы.")