from app import db, admin
from app.models import Users, Devices
from flask_admin.contrib.sqla import ModelView
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, \
    ValidationError, IPAddress
from werkzeug.security import generate_password_hash


class UsersView(ModelView):
    can_view_details = True
    can_set_page_size = True
    can_delete = True

    edit_modal = True
    create_modal = True
    details_modal = True

    column_default_sort = 'username'
    column_exclude_list = 'password'

    form_extra_fields = {
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
        )
    }

    def on_model_change(self, form, model, is_created):
        # Validação personalizada para verificar se o username já existe
        existing_user = db.session.execute(
            db.select(Users).filter_by(username=form.username.data)
        ).scalar_one_or_none()

        if existing_user and (is_created or existing_user.id != model.id):
            raise ValidationError('Usuário já cadastrado.')

        # Hash da senha
        if form.password.data:  # Apenas atualiza se a senha foi fornecida
            model.password = generate_password_hash(
                form.password.data,
                method='pbkdf2:sha256:600000'
            )


class DeviceView(ModelView):
    can_view_details = True
    can_set_page_size = True

    edit_modal = True
    details_modal = True

    form_extra_fields = {
        'ip_address': StringField(
            'IP Address',
            validators=[
                DataRequired(),
                IPAddress(ipv4=True)
            ]
        )
    }


def create_admin():
    admin.name = 'auto.clickip.local'
    admin.add_view(UsersView(Users, db.session))
    admin.add_view(DeviceView(Devices, db.session))
