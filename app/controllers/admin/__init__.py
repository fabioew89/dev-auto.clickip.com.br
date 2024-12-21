from app import db, admin
from app.models import Users, Devices
from flask_admin.contrib.sqla import ModelView
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, IPAddress
from werkzeug.security import generate_password_hash
from cryptography.fernet import Fernet

f = Fernet(Fernet.generate_key())


class UsersView(ModelView):
    can_edit = True
    can_delete = True
    can_create = True
    can_export = True
    can_view_details = True
    can_set_page_size = True

    edit_modal = True
    details_modal = True

    column_default_sort = 'username'
    # column_exclude_list = 'password'

    form_extra_fields = {
        'password': PasswordField(validators=[DataRequired(), Length(min=6)]),
        'Password Confirm': PasswordField(validators=[DataRequired(), EqualTo('password', message='Your password must be match')])  # noqa: E501
    }

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            # model.password = f.encrypt(form.password.data)
            model.password = generate_password_hash(
                form.password.data,
                method='pbkdf2:sha256:600000'
            )


class DeviceView(ModelView):
    can_edit = True
    can_delete = True
    can_create = True
    can_export = True
    can_view_details = True
    can_set_page_size = True

    edit_modal = True
    details_modal = True

    column_default_sort = 'hostname'

    form_extra_fields = {
        'ip_address': StringField('IP Address', validators=[DataRequired(), IPAddress(ipv4=True)])  # noqa: E501
    }


def create_admin():
    admin.name = 'auto.clickip.local'
    admin.add_view(UsersView(Users, db.session))
    admin.add_view(DeviceView(Devices, db.session))
