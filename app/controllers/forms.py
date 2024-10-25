from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class Form_Cad_User(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField(validators=[DataRequired(), Email(),Length(min=15, max=35)])
    submit = SubmitField('Salvar') # dont count like column

class Form_Cad_Future(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=4, max=32)])
    email = EmailField(validators=[DataRequired(), Email(), Length(min=4, max=32)])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField(validators=[
        DataRequired(), 
        Length(min=6),
        EqualTo('password', message='Password must match')
    ])
    submit = SubmitField('Cadastrar')

        