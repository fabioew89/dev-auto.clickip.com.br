from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db
from app.models.model import Table_Register, Table_Devices


def create_admin(app):
    admin = Admin(app, name='auto.clickip.local', template_mode='bootstrap3')
    admin.add_view(ModelView(Table_Register, db.session))
    admin.add_view(ModelView(Table_Devices, db.session))
