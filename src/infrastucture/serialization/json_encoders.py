from __future__ import annotations

import json
import re
from datetime import date, datetime
from typing import Any


class DateTimeEncoder(json.JSONEncoder):
    """Кастомный энкодер для поддержки дат в JSON."""

    ISO_DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    def default(self, o: Any) -> Any:
        """Метод для декодирования объектов типа datetime и date"""
        if isinstance(o, (date, datetime)):
            return o.isoformat()
        return super().default(o)

    @staticmethod
    def datetime_parser(some_dict: dict) -> dict:
        """Функция-помощник, которая ищет строки дат в словаре и конвертирует их в date."""
        for key, value in some_dict.items():
            # Если значение — строка, и она идеально подходит под формат YYYY-MM-DD
            if isinstance(value, str) and DateTimeEncoder.ISO_DATE_REGEX.match(value):
                try:
                    # Превращаем текст обратно в настоящий объект date
                    some_dict[key] = date.fromisoformat(value)
                except ValueError:
                    pass  # Если это была обычная строка, случайно похожая на дату
        return some_dict
