from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Alarm(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	#time = db.Column(db.String(64), index=True, unique=True)
	hour = db.Column(db.Integer, index=True)
	minute = db.Column(db.Integer, index=True)
	time = db.Column(db.Integer, index=True)
	active = db.Column(db.Boolean, default=True)
	repeat = db.Column(db.Boolean)
	label = db.Column(db.String(64))
	duration = db.Column(db.Integer)
	monday = db.Column(db.Boolean)
	tuesday = db.Column(db.Boolean)
	wednesday = db.Column(db.Boolean)
	thursday = db.Column(db.Boolean)
	friday = db.Column(db.Boolean)
	saturday = db.Column(db.Boolean)
	sunday = db.Column(db.Boolean)
	
	def __repr__(self):
		return '<Alarm {}>'.format(self.id)



@login.user_loader
def load_user(id):
	return User.query.get(int(id))