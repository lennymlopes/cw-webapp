from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Alarm(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.String(64), index=True, unique=True)
	active = db.Column(db.Boolean, index=True, unique=True)
	repeat = db.Column(db.Integer)
	label = db.Column(db.String(64))

	def __repr__(self):
		return '<Alarm {}>'.format(self.id)
