from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError, IPAddress
from app.models.model import Tab_Register

class Form_Register(FlaskForm):
    def validate_email(self, check_email):
        email = Tab_Register.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError('Email ja cadastrado!!!')        
        
    email               = EmailField(validators=   [DataRequired(), Length(min=15, max=35), Email()])
    password            = PasswordField(validators=[DataRequired(), Length(min=6)])
    password_confirm    = PasswordField(validators=[DataRequired(), EqualTo('password', message='Password must match')])
    submit              = SubmitField('Cadastrar')

class Form_Login(FlaskForm):
    email_login         = EmailField(validators=[DataRequired()])
    password_login      = PasswordField(validators=[DataRequired()])
    submit_login        = SubmitField('Entrar')
    
class Form_Cad_User(FlaskForm):
    username          = StringField(validators=[DataRequired(), Length(min=3, max=20)])
    user_pass         = PasswordField(validators=[DataRequired(), Length(min=6)])
    user_pass_confirm = PasswordField(DataRequired(), EqualTo('password', message='Password must match'))
    submit_login      = SubmitField('Entrar')
    
class Form_Devices(FlaskForm):
    device_name = StringField(validators=[DataRequired(),Length(min=5)])
    ip_address  = StringField(validators=[DataRequired(IPAddress())])
    subit       = SubmitField('Cadastrar')