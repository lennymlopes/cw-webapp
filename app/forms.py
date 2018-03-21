from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, DateField, Field
from wtforms.validators import DataRequired
from wtforms_components import TimeField

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class NewAlarmForm(Field):
	time = TimeField('Time')
	submit = SubmitField('Save')