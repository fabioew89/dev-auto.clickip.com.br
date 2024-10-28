from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from app.models.model import Tab_User, Tab_New_Users

class Form_Cad_User(FlaskForm):
    def validate_username(self, check_user):
        user = Tab_User.query.filter_by(username=check_user.data).first()
        if user:
            raise ValidationError('Usuario ja cadastrado!!!')

    def validate_email(self, check_email):
        email = Tab_User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError('Email ja cadastrado!!!')
              
    username = StringField(validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField(validators=[DataRequired(), Email(),Length(min=15, max=35)])
    submit = SubmitField('Salvar') # dont count like column



class Form_New_Cad(FlaskForm):
    def validate_email(self, check_email):
        email = Tab_New_Users.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError('Email ja cadastrado!!!')
            
    email            = EmailField(validators=[DataRequired(), Email(), Length(min=4, max=32)])
    password         = PasswordField(validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField(validators=[DataRequired(),EqualTo('password', message='Password must match')])
    submit = SubmitField('Vai')

        