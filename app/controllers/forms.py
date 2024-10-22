from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired

class form_cad_user(Form):
    username = StringField('Username', [validators.length(min=4, max=25)])
    email = StringField('Email', [
        validators.DataRequired()
    ])