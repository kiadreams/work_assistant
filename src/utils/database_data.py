from __future__ import annotations

from typing import TYPE_CHECKING

import json
import shutil
from pathlib import Path

from sqlalchemy import insert

if TYPE_CHECKING:
    from sqlalchemy.engine import Engine
    from database.db_manager import DatabaseManager


def create_clean_dir(dir_name: str) -> None:
    # 1. Удаляем папку с указанным именеи, если сущеуствует
    folder_name = Path(dir_name)
    if folder_name.exists() and folder_name.is_dir():
        try:
            shutil.rmtree(folder_name)
            print(f"Папка '{folder_name}' и все ее содержимое успешно удалены.")
        except OSError as e:
            print(f"Ошибка при удалении папки {folder_name}: {e}")
    else:
        print(f"Папка '{folder_name}' не найдена или не является директорией.")

    # 2. Создаем новую пустую папку с тем же именем
    try:
        folder_name.mkdir()
        print(f"Новая пустая папка '{folder_name}' успешно создана.")
    except OSError as e:
        print(f"Ошибка при создании папки {folder_name}: {e}")


def export_data_to_json_files(data_dict, target_dir: Path) -> None:
    dir_name = Path("data_of_all_tables")
    target_dir_name = target_dir / dir_name
    create_clean_dir(target_dir_name)
    for table_name, records in data_dict.items():
        # Убираем внутренние атрибуты SQLAlchemy из словарей
        clean_records = []
        for record in records:
            clean_record = {k: v for k, v in record.items() if not k.startswith('_sa_')}
            clean_records.append(clean_record)

        file_path = target_dir_name / f"{table_name}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(clean_records, f, ensure_ascii=False, indent=4)
        print(f"Экспортировано {len(clean_records)} записей в {file_path}")
    print("Экспорт завершен.")


def import_from_json_files(directory: Path, db_manager: DatabaseManager) -> None:
    target_dir = directory / "data_of_all_tables"
    # Определяем порядок импорта, чтобы избежать ошибок внешних ключей
    import_order = ["divisions", "departments", "employee_positions", "employees",
                    "equipment_locations", "equipment", "work_types", "works",
                    "work_tasks", "work_orders"]

    for table_name in import_order:
        file_path = target_dir / f"{table_name}.json"
        if not file_path.exists():
            print(f"Файл {file_path} не найден, пропуск.")
            continue

        with open(file_path, "r", encoding='utf-8') as f:
            data_to_insert = json.load(f)

        # Вставляем полученные данные в указанную таблицу...
        db_manager.insert_data_to_table_db(table_name, data_to_insert)
    print("Импорт завершен.")
