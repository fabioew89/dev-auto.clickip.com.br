from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, IPAddress, NumberRange


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(max=30)
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(max=30)
        ])
    checkbox = BooleanField(
        'Remember me!',
        default=True
        )
    submit = SubmitField('Entrar')


class NetworkForm(FlaskForm):
    hostname = SelectField(
        'Hostname', choices=[]
    )
    username = StringField(
        'Username', validators=[
            DataRequired(),
            Length(min=3, max=30)
        ]
    )
    password = PasswordField(
        'Password', validators=[
            DataRequired(),
            Length(min=6),
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
