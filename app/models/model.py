from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Tab_User(db.Model):

    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    # password: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
