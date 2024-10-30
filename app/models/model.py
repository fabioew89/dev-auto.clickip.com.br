from app import db, login_manager
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Tab_Register.query.get(int(user_id))

class Tab_Register(db.Model, UserMixin):
    __tablename__ = 'Tab_Register'
    id:    Mapped[int] = mapped_column(primary_key=True)
    email:    Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'
    