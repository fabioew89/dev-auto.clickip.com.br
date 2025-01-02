from app import db, admin
from app.models import Users, Devices
from flask_admin.contrib.sqla import ModelView
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, \
    Length, EqualTo, IPAddress, InputRequired
from cryptography.fernet import Fernet


class UsersView(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True
    can_view_details = True
    can_set_page_size = True

    edit_modal = True
    details_modal = True

    column_default_sort = 'username'
    column_exclude_list = 'password'

    form_extra_fields = {
        'username': StringField(
            validators=[
                DataRequired(),
                Length(min=5, max=30)
            ]
        ),
        'password': PasswordField(
            validators=[
                DataRequired(),
                Length(min=6)
            ]
        ),
        'Password Confirm': PasswordField(
            validators=[
                DataRequired(),
                EqualTo('password', message='Your password must be match')
            ]
        ),
    }

    def on_model_change(self, form, model, is_created):
        f = Fernet(b'bdilxeLGCHnJo-2HtofB9wGcXaUV7D5NZgxh5Nt5fpg=')
        if form.password.data:
            model.password = f.encrypt(form.password.data.encode('utf-8'))


class DeviceView(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_export = True
    can_view_details = True
    can_set_page_size = True

    edit_modal = True
    details_modal = True

    column_default_sort = 'hostname'

    form_extra_fields = {
        'ip_address': StringField(
            'IP Address', validators=[
                InputRequired(),
                IPAddress(ipv4=True)
                ]
            ),
        }


def create_admin():
    admin.name = 'auto.clickip.local'
    admin.add_view(UsersView(Users, db.session))
    admin.add_view(DeviceView(Devices, db.session))
