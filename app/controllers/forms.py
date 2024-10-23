from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class Form_Cad_User(FlaskForm):
    username = StringField(name='username', id='username', validators=[DataRequired(), Length(min=4, max=32)])
    email = EmailField(name='email', id='email', validators=[DataRequired(), Length(min=4, max=32)])
    password = PasswordField(name='password', id='password', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField(name='password_confirm', id='password_confirm', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField(validators=[DataRequired()])