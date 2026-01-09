from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from .config import DATABASE_URL


class Base(DeclarativeBase):
    pass


class DatabaseManager:
    def __init__(self) -> None:
        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = sessionmaker(autoflush=False, bind=self.engine)

    def create_db_tables(self) -> None:
        print(f"Подключение к базе данных {self.engine.url} и создание таблиц...")
        # --- ЭТА КОМАНДА СОЗДАЕТ ТАБЛИЦЫ ---
        # Она проверяет все импортированные классы, наследуемые от Base,
        # и создает таблицы, если они еще не существуют.
        Base.metadata.create_all(self.engine)
        print("Таблицы успешно созданы.")

    @contextmanager
    def session_scope(self) -> Generator[Session, None, None]:
        """
        Предоставляет транзакционную сессию в качестве контекстного менеджера.
        Автоматически коммитит при успехе и откатывает при ошибке.
        """
        session = self.SessionLocal()
        try:
            yield session  # Предоставляет сессию для использования в блоке 'with'
            session.commit()  # Коммит транзакции при успешном выходе из блока 'with'
        except:
            session.rollback()  # Откат транзакции в случае исключения
            raise  # Повторное возбуждение исключения
        finally:
            session.close()  # Гарантированное закрытие сессии (возвращение в пул)
