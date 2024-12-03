from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo, \
    ValidationError, IPAddress, NumberRange
import ipaddress
from app import db
from app.models.model import Table_Register


def validate_ipv6(form, field):
    try:
        ipaddress.IPv6Address(field.data)
    except ValueError:
        raise ValidationError('Invalid IPv6 address format.')


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
        'Username', validators=[DataRequired()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired()])
    submit = SubmitField('Entrar')


class Form_Devices(FlaskForm):
    hostname = StringField(
        'Hostname', validators=[DataRequired(), Length(min=3, max=10)])
    ip_address = StringField(
        'IP Address', validators=[DataRequired(), IPAddress()]
    )
    submit = SubmitField('Cadastrar')


class Network_Form(FlaskForm):
    hostname = SelectField(
        'Hostname', choices=[]
    )
    username = SelectField(
        'Username', choices=[]
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )
    unit_vlan = IntegerField(
        'Unit VLAN', validators=[
            DataRequired(),
            NumberRange(min=1, max=4096)
        ]
    )
    description = StringField(
        'Description', validators=[DataRequired()]
    )
    bandwidth = IntegerField(
        'Bandwidth', validators=[DataRequired()]
    )
    ipv4_gw = StringField(
        'IPv4 Address', validators=[
            DataRequired(),
            IPAddress(ipv4=True)
        ]
    )
    ipv6_gw = StringField(
        'IPv6 Gateway', validators=[
            DataRequired(),
            validate_ipv6
        ]
    )
    ipv6_cli = StringField(
        'IPv6 Client', validators=[
            DataRequired(),
            validate_ipv6
        ]
    )
    ipv6_48 = StringField(
        'IPv6 /48', validators=[
            DataRequired(),
            validate_ipv6
        ]
    )
    submit = SubmitField('Enviar')
