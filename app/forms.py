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
	monday = BooleanField('Monday')
	tuesday = BooleanField('Tuesday')
	wednesday = BooleanField('Wednesday')
	thursday = BooleanField('Thursday')
	friday = BooleanField('Friday')
	saturday = BooleanField('Saturday')
	sunday = BooleanField('Sunday')
	repeat = RadioField('Repeat', choices=[('0','never'),('1','weekly'),('2','biweekly')])
	submit = SubmitField('Save')

class SettingsForm(FlaskForm):
	#theme = BooleanField('Dark')
	advanced = BooleanField('Advanced Mode')
	time_format = BooleanField('Time Format')
	submit = SubmitField('Save')





