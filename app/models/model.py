from app import db
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)