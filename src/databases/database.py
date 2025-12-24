from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from sqlalchemy.orm.session import Session


class Base(DeclarativeBase):
    pass


DATABASE_URL = "sqlite:///instance/work_database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def create_db_tables() -> None:
    print(f"Подключение к базе данных {engine.url} и создание таблиц...")

    # --- ЭТА КОМАНДА СОЗДАЕТ ТАБЛИЦЫ ---
    # Она проверяет все импортированные классы, наследуемые от Base,
    # и создает таблицы, если они еще не существуют.
    Base.metadata.create_all(engine)

    print("Таблицы успешно созданы.")


# Вспомогательная функция для получения сессии (часто используется в FastAPI/Flask)
def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
