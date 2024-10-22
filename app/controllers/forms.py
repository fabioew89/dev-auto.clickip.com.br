from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, validators, SubmitField

class CadastroForm(FlaskForm):
    username = StringField(label='username')
    email = EmailField(label='email')
    password = PasswordField(label='password')
    password_confirm = PasswordField(label='confir password')
    submit = SubmitField(label='Enviar')