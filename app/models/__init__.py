from app import db, lm
from flask_login import UserMixin


@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def __str__(self):
        return super().__str__(self.username)


class Devices(db.Model):
    __tablename__ = 'Devices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=True)
    ip_address = db.Column(db.String, nullable=True)

    def __str__(self):
        return super().__str__(self.hostname, self.ip_address)
