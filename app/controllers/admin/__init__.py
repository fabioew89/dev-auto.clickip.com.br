from app import db, admin
from app.models import Users, Devices
from flask_admin.contrib.sqla import ModelView


def create_admin():
    admin.name = 'auto.clickip.local'
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Devices, db.session))
