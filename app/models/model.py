from app import db, login_manager
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Table_Register.query.get(int(user_id))

class Table_Register(db.Model, UserMixin):
    __tablename__ = 'Table_Register'
    id:         Mapped[int] = mapped_column(primary_key=True)
    username:   Mapped[str] = mapped_column(unique=True, nullable=False)
    password:   Mapped[str] = mapped_column(unique=True, nullable=False)
    
    def __str__(self):
        return self.id, self.username

class Table_Devices(db.Model):
    __tablename__ = 'Table_Devices'
    id:         Mapped[int] = mapped_column(primary_key=True)
    hostname:   Mapped[str] = mapped_column(unique=True, nullable=False)
    ip_address: Mapped[str] = mapped_column(unique=True, nullable=False)
    
    def __str__(self):
        return self.hostname, self.ip_address
