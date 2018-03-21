from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField, SelectField, validators, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, NumberRange
from wtforms_components import IntegerField
from werkzeug.datastructures import MultiDict



class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class NewAlarmForm(FlaskForm):

	hours = IntegerField('Hour', validators=[NumberRange(min=0, max=23),DataRequired()])
	minutes = IntegerField('Minute', validators=[NumberRange(min=0, max=59),DataRequired()])
	#days = SelectMultipleField('Days', choices=[('1','Monday'),('2','Tuesday'),('3','Tuesday'),('4','Tuesday'),('5','Tuesday')] )
	#alt_days = RadioField('Days', choices=[('1','Monday'),('2','Tuesday'),('3','Tuesday'),('4','Tuesday'),('5','Tuesday')] )
	monday = BooleanField('Monday')
	tuesday = BooleanField('Tuesday')
	wednesday = BooleanField('Wednesday')
	thursday = BooleanField('Thursday')
	friday = BooleanField('Friday')
	saturday = BooleanField('Saturday')
	sunday = BooleanField('Sunday')

	repeat = RadioField('Repeat', choices=[('0','never'),('1','weekly'),('2','biweekly')])
	submit = SubmitField('Save')



