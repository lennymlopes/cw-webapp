from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField, SelectField, validators, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, NumberRange, ValidationError, Email, EqualTo
from wtforms_components import IntegerField
from werkzeug.datastructures import MultiDict
from app.models import User


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')




class NewAlarmForm(FlaskForm):

	hours = IntegerField('Hour', validators=[NumberRange(min=0, max=23),DataRequired()])
	minutes = IntegerField('Minute', validators=[NumberRange(min=0, max=59),DataRequired()])
	monday = BooleanField('M')
	tuesday = BooleanField('T')
	wednesday = BooleanField('W')
	thursday = BooleanField('T')
	friday = BooleanField('F')
	saturday = BooleanField('S')
	sunday = BooleanField('S')
	repeat = BooleanField('Repeat')
	label = StringField('Label')
	submit = SubmitField('Save')

class SettingsForm(FlaskForm):
	theme = BooleanField('Dark Theme')
	stream = StringField('Webradio Link')
	delete = SubmitField('Delete All Alarms')
	duration = IntegerField('Sunrise Duration')

	# advanced = BooleanField('Advanced Mode')
	#time_format = BooleanField('Time Format')
	submit = SubmitField('Save')





