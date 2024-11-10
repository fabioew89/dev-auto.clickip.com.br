from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, IPAddress
from app.models.model import Tab_Register

class Form_Register(FlaskForm):
    def validate_username(self, field):
        username = db.session.execute(db.select(Tab_Register).filter_by(username=field.data)).scalar_one_or_none()
        if username:
            raise ValidationError('Usuário já cadastrado')

    username         = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password         = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='As senhas devem coincidir')])
    submit           = SubmitField('Cadastrar')

class Form_Login(FlaskForm):
    username         = StringField(validators=[DataRequired()])
    password         = PasswordField(validators=[DataRequired()])
    submit           = SubmitField('Entrar')

##### ##### ##### ##### ##### ##### ##### ##### ##### #####     
    
class Form_Cad_User(FlaskForm):
    username            = StringField(validators=   [DataRequired(), Length(min=3, max=20)])
    user_pass           = PasswordField(validators= [DataRequired(), Length(min=6)])
    user_pass_confirm   = PasswordField(DataRequired(), EqualTo('password', message='Password must match'))
    submit_login        = SubmitField('Entrar')
    
class Form_Devices(FlaskForm):
    hostname            = StringField(validators=   [DataRequired(), Length(min=3, max=10)])
    ip_address          = StringField(validators=   [DataRequired(), IPAddress()])
    submit              = SubmitField('Cadastrar')