from app import db, lm
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin


@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id:         Mapped[int] = mapped_column(primary_key=True)
    username:   Mapped[str] = mapped_column(unique=True, nullable=False)
    password:   Mapped[str] = mapped_column(unique=True, nullable=False)

    def __str__(self):
        return self.id, self.username


class Devices(db.Model):
    __tablename__ = 'Devices'
    id:         Mapped[int] = mapped_column(primary_key=True)
    hostname:   Mapped[str] = mapped_column(unique=True, nullable=False)
    ip_address: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __str__(self):
        return self.hostname, self.ip_address
''