from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    SelectField  # FloatField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, \
    ValidationError, IPAddress  # Optional
from app.models.model import Table_Register  # Table_Devices
from app import db


class Form_Register(FlaskForm):
    def validate_username(self, field):
        username = db.session.execute(
            db.select(Table_Register).filter_by(username=field.data)
        ).scalar_one_or_none()
        if username:
            raise ValidationError('Usuário já cadastrado')

    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=25),
        ])

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6),
        ])

    password_confirm = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='As senhas devem coincidir')
        ])

    submit = SubmitField('Cadastrar')


class Form_Login(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Entrar')


class Form_Devices(FlaskForm):
    hostname = StringField(validators=[
        DataRequired(),
        Length(min=3, max=10)
        ])

    ip_address = StringField(validators=[
        DataRequired(),
        IPAddress()
        ])

    submit = SubmitField('Cadastrar')


class Network_Form(FlaskForm):
    device = SelectField('Devices', choices=[])


#     unit_vlan = IntegerField('Unit VLAN', validators=[DataRequired()])
#     description = StringField('Description', validators=[Optional()])
#     ipv4_address = StringField('IPv4 Address', validators=[IPAddress(ipv4=True), Optional()])
#     bandwith = FloatField('Bandwidth', validators=[Optional()])
#     ipv6_gw = StringField('IPv6 Gateway', validators=[IPAddress(ipv6=True), Optional()])
#     ipv6_cli = StringField('IPv6 Client', validators=[IPAddress(ipv6=True), Optional()])
#     ipv6_48 = StringField('IPv6 /48', validators=[Optional()])
#     username = SelectField('Username', choices=[('fabio.ewerton', 'fabio.ewerton'), ('admin', 'admin')], validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Enviar')
