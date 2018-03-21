from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField, SelectField, validators
from wtforms.validators import DataRequired, NumberRange
from wtforms_components import IntegerField
from werkzeug.datastructures import MultiDict



class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class NewAlarmForm(FlaskForm):
	hours = IntegerField('Hour', validators=[NumberRange(min=0, max=23, message='lol')])
	minutes = IntegerField('Minute', validators=[NumberRange(min=0, max=59, message='lol')])
	submit = SubmitField('Save')
