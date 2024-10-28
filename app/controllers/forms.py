from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from app.models.model import Tab_Register

class Form_Register(FlaskForm):
    def validate_email(self, check_email):
        email = Tab_Register.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError('Email ja cadastrado!!!')        
        
    email            = EmailField(validators=   [DataRequired(), Length(min=15, max=35), Email()])
    password         = PasswordField(validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField(validators=[DataRequired(), EqualTo('password', message='Password must match')])
    submit = SubmitField('Cadastrar')
