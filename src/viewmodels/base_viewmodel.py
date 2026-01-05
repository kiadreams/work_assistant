from sqlalchemy.orm import Session

from ..database.database import SessionLocal


class BaseViewModel:
    def __init__(self) -> None:
        self.session: Session = SessionLocal()
