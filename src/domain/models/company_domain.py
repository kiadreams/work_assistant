from __future__ import annotations

from typing import Any


class CompanyDomain:
    def __init__(
        self,
        *,
        company_id: int,
        name: str,
        full_name: str | None = None,
    ) -> None:
        self.id = company_id
        self.name = name
        self.full_name = full_name

    @property
    def model_data(self) -> dict[str, Any]:
        return vars(self)
