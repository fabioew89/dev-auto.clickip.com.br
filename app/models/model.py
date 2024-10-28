from app import db, bcrypt
from sqlalchemy.orm import Mapped, mapped_column

class Tab_User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] =       mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] =    mapped_column(unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Tab_New_Users(db.Model):
    __tablename__ = 'Tab_New_Users'
    keyid:    Mapped[int] = mapped_column(primary_key=True)
    email:    Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(unique=True, nullable=False)
    
    @property
    def password_bcrypt(self):
        return self.password_bcrypt
    
    @password_bcrypt.setter
    def password_bcrypt(self, password_plain_text):
        self.password = bcrypt.generate_password_hash(password_plain_text).decode('utf-8')

    def __repr__(self):
        return f'<User {self.username}>'
