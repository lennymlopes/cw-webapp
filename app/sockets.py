from flask_socketio import SocketIO, emit
from app import app, db, alarms
from app.models import Alarm

socketio = SocketIO(app)

@socketio.on('update')
def update(parameter, data):
	print('Updated ' + parameter + ': ' + data)

@socketio.on('delete_alarm')
def delete(id):
		Alarm.query.filter_by(id=int(id)).delete()
		db.session.commit()
		print('Alarm ' + id + ' deleted')

@socketio.on('set_color')
def set_color(color, value):
		print('SPI send: ' + color + ' set to ' + value)
		alarms.get_next()