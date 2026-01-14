from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, insert
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

    def get_all_data_from_db(self) -> dict[str, str]:
        """Извлекает данные из всех таблиц, определенных в Base."""
        all_data = {}
        with self.session_scope() as session:
            for mapper in Base.registry.mappers:
                model_class = mapper.class_
                table_name = model_class.__tablename__
                print(f"Извлечение данных из таблицы: {table_name}")
                query_result = session.query(model_class).all()
                data_as_dicts = []
                for row in query_result:
                    clean_record = {column.name: getattr(row, column.name) for column in
                                    mapper.columns}
                    data_as_dicts.append(clean_record)
                all_data[table_name] = data_as_dicts
        return all_data

    def insert_data_to_table_db(self, table_name: str, data_to_insert: dict[str, str]) -> None:
        with self.engine.connect() as connection:
            target_table = None
            for mapper in Base.registry.mappers:
                if mapper.tables[0].name == table_name:
                    target_table = mapper.tables[0]
                    break
            if target_table is not None and data_to_insert:
                print(f"Импорт {len(data_to_insert)} записей в таблицу {table_name}...")
                # Используем bulk_insert_mappings для быстрой вставки
                connection.execute(insert(target_table), data_to_insert)
            connection.commit()

