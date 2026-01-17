import json
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator

import pandas as pd
from sqlalchemy import create_engine, insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from src.core.constants import DbTables
from src.database.config import CSV_TABLE_DATA_DIR, DATABASE_URL, JSON_TABLE_DATA_DIR
from src.utils.file_utils import create_clean_dir


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

    @property
    def all_table_data(self) -> dict[Any, list[dict[str, Any]]]:
        """Извлекает данные из всех таблиц, определенных в Base."""
        all_data = {}
        with self.session_scope() as session:
            for mapper in Base.registry.mappers:
                model_class = mapper.class_
                table_name = model_class.__tablename__
                query_result = session.query(model_class).all()
                data_as_dicts = []
                for row in query_result:
                    clean_record = {
                        column.name: getattr(row, column.name) for column in mapper.columns
                    }
                    data_as_dicts.append(clean_record)
                all_data[table_name] = data_as_dicts
        return all_data

    def insert_to_table_db_from_json(
        self, table_name: str, data_to_insert: dict[Any, list[dict[str, Any]]]
    ) -> None:
        with self.engine.connect() as connection:
            target_table = None
            for mapper in Base.registry.mappers:
                if mapper.tables[0].name == table_name:
                    target_table = mapper.tables[0]
                    break
            if target_table is not None and data_to_insert:
                # Используем bulk_insert_mappings для быстрой вставки
                connection.execute(insert(target_table), data_to_insert)
            connection.commit()

    def export_to_csv_files(self) -> None:
        target_dir = Path(CSV_TABLE_DATA_DIR)
        create_clean_dir(target_dir)
        for mapper in Base.registry.mappers:
            table_name = mapper.tables[0].name
            file_path = target_dir / f"{table_name}.csv"

            try:
                df = pd.read_sql_table(table_name=table_name, con=self.engine)
                df.to_csv(file_path, index=False)
            except SQLAlchemyError as e:
                print(f"Ошибка базы данных при экспорте таблицы {table_name}: {e}")
        print("Экспорт данных в файлы CSV закончен")

    def export_to_json_files(self) -> None:
        target_dir = Path(JSON_TABLE_DATA_DIR)
        create_clean_dir(target_dir)
        for table_name, records in self.all_table_data.items():
            # Убираем внутренние атрибуты SQLAlchemy из словарей
            clean_records = []
            for record in records:
                clean_record = {k: v for k, v in record.items() if not k.startswith("_sa_")}
                clean_records.append(clean_record)
            file_path = target_dir / f"{table_name}.json"
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(clean_records, f, ensure_ascii=False, indent=4)
        print("Экспорт данных в файлы JSON закончен")

    def import_from_json_files(self) -> None:
        target_dir = Path(JSON_TABLE_DATA_DIR)
        # Определяем порядок таблиц для импорта, чтобы избежать ошибок внешних ключей (DbTables)
        for table_name in DbTables:
            file_path = target_dir / f"{table_name}.json"
            if not file_path.exists():
                print(f"Файл {file_path} не найден, пропуск.")
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                data_to_insert = json.load(f)

            # Вставляем полученные данные в указанную таблицу...
            try:
                self.insert_to_table_db_from_json(table_name, data_to_insert)
            except SQLAlchemyError as e:
                print(
                    f"Ошибка несоответствия структуры таблиц"
                    f" или дублирования данных {table_name}: {e}"
                )
        print("Импорт завершен из JSON файлов завершен.")

    def import_from_csv_files(self) -> None:
        target_dir = Path(CSV_TABLE_DATA_DIR)
        # Определяем порядок таблиц для импорта, чтобы избежать ошибок внешних ключей (DbTables)
        for table_name in DbTables:
            file_path = target_dir / f"{table_name}.csv"
            if not file_path.exists():
                print(f"Файл {file_path} не найден, пропуск.")
                continue

            try:
                df = pd.read_csv(file_path, encoding="utf-8")
                df.to_sql(table_name, con=self.engine, if_exists="append", index=False)
            except SQLAlchemyError as e:
                print(f"Ошибка базы данных при экспорте таблицы {table_name}: {e}")
        print("Импорт завершен из CSV файлов завершен.")
