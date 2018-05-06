from flask_socketio import SocketIO, emit
from app import app, db, alarms
from app.models import Alarm

socketio = SocketIO(app)

moodlight = False

@socketio.on('update')
def update(id, parameter, data):
	alarm = Alarm.query.filter_by(id=int(id)).first()
	if(parameter == 'monday'):
		print(alarm.monday)
		alarm.monday = not alarm.monday
	if(parameter == 'tuesday'):
		alarm.tuesday = not alarm.tuesday
	if(parameter == 'wednesday'):
		alarm.wednesday = not alarm.wednesday
	if(parameter == 'thursday'):
		alarm.thursday = not alarm.thursday
	if(parameter == 'friday'):
		alarm.friday = not alarm.friday
	if(parameter == 'saturday'):
		alarm.saturday = not alarm.saturday
	if(parameter == 'sunday'):
		alarm.sunday = not alarm.sunday

	if(parameter == 'on'):
		alarm.active = not alarm.active

	if(parameter == 'moodlight'):
		moodlight = not moodlight
		if(moodlight):
			print('Moodlight On')
		else:
			print('Moodlight Off')

	db.session.commit()

	print('Updated ' + parameter + ': ' + data)

@socketio.on('delete_alarm')
def delete(id):
		Alarm.query.filter_by(id=int(id)).delete()
		db.session.commit()
		print('Alarm ' + id + ' deleted')

@socketio.on('set_color')
def set_color(color, value):
		print('SPI send: ' + color + ' set to ' + value)
		alarms.check_for_alarms()
