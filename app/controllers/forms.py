from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class Form_Cad_User(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=4, max=32)])
    email = EmailField(validators=[DataRequired(), Length(min=4, max=32)])
    submit = SubmitField('Commit')

class Form_Cad_Future(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=4, max=32)])
    email = EmailField(validators=[DataRequired(), Length(min=4, max=32)])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField(validators=[
        DataRequired(), 
        Length(min=6),
        EqualTo('password', message='Password must match')
    ])
    submit = SubmitField('Cadastrar')

        