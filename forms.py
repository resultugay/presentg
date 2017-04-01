from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, NumberRange, Optional


from datetime import datetime


class LoginForm(FlaskForm):
    email = StringField('email' , validators=[DataRequired()])
    password = StringField('password' , validators=[DataRequired()])

