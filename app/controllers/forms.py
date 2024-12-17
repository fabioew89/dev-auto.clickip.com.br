from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    SelectField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, \
    ValidationError, IPAddress, NumberRange
from app import db
from app.models import Users


class Form_Register(FlaskForm):
    def validate_username(self, field):
        username = db.session.execute(
            db.select(Users).filter_by(username=field.data)
        ).scalar_one_or_none()
        if username:
            raise ValidationError('Usuário já cadastrado')

    username = StringField(
        'Username', validators=[
            DataRequired(),
            Length(min=3, max=25)
        ]
    )
    password = PasswordField(
        'Password', validators=[
            DataRequired(),
            Length(min=6)
        ]
    )
    password_confirm = PasswordField(
        'Confirm Password', validators=[
            DataRequired(),
            EqualTo('password', message='As senhas devem coincidir')
        ]
    )
    submit = SubmitField('Cadastrar')


class Form_Login(FlaskForm):
    username = StringField(
        'Username', validators=[
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password', validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Entrar')


class Form_Devices(FlaskForm):
    hostname = StringField(
        'Hostname', validators=[
            DataRequired(),
            Length(min=3, max=30)
        ]
    )
    ip_address = StringField(
        'IP Address', validators=[
            DataRequired(),
            IPAddress()
        ]
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
        'Password', validators=[
            DataRequired()
        ]
    )
    unit_vlan = IntegerField(
        'Unit VLAN', validators=[
            DataRequired(),
            NumberRange(min=1, max=4096)
        ]
    )
    description = StringField(
        'Description', validators=[
            DataRequired()
        ]
    )
    bandwidth = IntegerField(
        'Bandwidth', validators=[
            DataRequired(),
            NumberRange(min=1, max=9999)
        ]
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
            IPAddress(ipv6=True)
        ]
    )
    ipv6_cli = StringField(
        'IPv6 Client', validators=[
            DataRequired(),
            IPAddress(ipv6=True)
        ]
    )
    ipv6_48 = StringField(
        'IPv6 /48', validators=[
            DataRequired(),
            IPAddress(ipv6=True)
        ]
    )
    submit = SubmitField('Commitar')
