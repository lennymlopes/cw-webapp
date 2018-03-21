from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm ,NewAlarmForm
from werkzeug.datastructures import MultiDict

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Lenny'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

@app.route('/new', methods=['GET', 'POST'])
def new():
	form = NewAlarmForm()
	if form.validate_on_submit():
		flash('New alarm added at {}:{}, on {}'.format(
			form.hours.data, form.minutes.data))
		return redirect(url_for('index'))
	return render_template('alarm.html', title='Add Alarms', form=form)