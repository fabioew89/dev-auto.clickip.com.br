from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    SelectField, IntegerField, FloatField

from wtforms.validators import DataRequired, Length, EqualTo, \
    ValidationError, IPAddress  # Optional

from app import db
from app.models.model import Table_Register


class Form_Register(FlaskForm):
    def validate_username(self, field):
        username = db.session.execute(
            db.select(Table_Register).filter_by(username=field.data)
        ).scalar_one_or_none()
        if username:
            raise ValidationError('Usuário já cadastrado')

    username = StringField(
        'Username', validators=[DataRequired(), Length(min=3, max=25)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6)]
    )
    password_confirm = PasswordField(
        'Confirm Password', validators=[
            DataRequired(),
            EqualTo('password', message='As senhas devem coincidir')]
    )
    submit = SubmitField('Cadastrar')


class Form_Login(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired()]
    )
    password = PasswordField(
        'password', validators=[DataRequired()])
    submit = SubmitField('Entrar')


class Form_Devices(FlaskForm):
    hostname = StringField(
        'hostname', validators=[DataRequired(), Length(min=3, max=10)])
    ip_address = StringField(
        'ip_address', validators=[DataRequired(), IPAddress()]
    )
    submit = SubmitField('Cadastrar')


class Network_Form(FlaskForm):
    device = SelectField(
        'Devices', choices=[]
    )
    username = SelectField(
        'Username', choices=[]
    )
    password = PasswordField(
        'Password',     validators=[DataRequired()]
    )
    unit_vlan = IntegerField(
        'Unit VLAN',    validators=[DataRequired()]
    )
    description = StringField(
        'Description',  validators=[DataRequired()]
    )
    bandwith = FloatField(
        'Bandwidth',    validators=[DataRequired()]
    )
    ipv4_gw = StringField(
        'IPv4 Address', validators=[DataRequired(), IPAddress(ipv4=True)]
    )
    ipv6_gw = StringField(
        'IPv6 Gateway', validators=[DataRequired(), IPAddress(ipv6=True)]
    )
    ipv6_cli = StringField(
        'IPv6 Client',  validators=[DataRequired(), IPAddress(ipv6=True)]
    )
    ipv6_48 = StringField(
        'IPv6 /48',     validators=[DataRequired(), IPAddress(ipv6=True)]
    )
    submit = SubmitField('Enviar')
