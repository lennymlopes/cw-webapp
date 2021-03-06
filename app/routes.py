from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm ,NewAlarmForm, RegistrationForm, SettingsForm
from werkzeug.datastructures import MultiDict
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Alarm

@app.route('/')
@app.route('/index')
@login_required
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
	alarms = Alarm.query.all()
	return render_template('index.html', title='Home', posts=posts, alarms=alarms)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
	form = NewAlarmForm()
	if form.validate_on_submit():
		alarm = Alarm(time=(form.hours.data*3600+form.minutes.data*60),\
									hour=form.hours.data,\
									minute=form.minutes.data,\
									repeat=form.repeat.data,\
									label=form.label.data,\
									monday=form.monday.data,\
									tuesday=form.tuesday.data,\
									wednesday=form.wednesday.data,\
									thursday=form.thursday.data,\
									friday=form.friday.data,\
									saturday=form.saturday.data,\
									sunday=form.sunday.data)
		db.session.add(alarm)
		db.session.commit()
		# flash('New alarm "{}"added at {}:{}, on '.format(
		# 	form.label.data, form.hours.data, form.minutes.data))
		return redirect(url_for('index'))
	return render_template('alarm.html', title='Add Alarms', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
	form = SettingsForm()
	if form.validate_on_submit():
		flash('Settings Saved')
		return redirect(url_for('index'))
	return render_template('settings.html', title='Settings', form=form)