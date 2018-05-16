from flask_socketio import SocketIO, emit
from app import app, db, alarms
from app.models import Alarm

socketio = SocketIO(app)

red = 0
green = 0
blue = 0
state = 0

moodlight = False

@socketio.on('update')
def update(id, parameter, data):
	global moodlight
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
		socketio.emit('update',('moodlight', moodlight))
	db.session.commit()

	print('Updated ' + parameter + ': ' + data)


@socketio.on('moodlight')
def moodlight_enable():
	global moodlight
	# global state
	moodlight = not moodlight
	if (moodlight):
		print('SPI send: Moodlight on:'\
								+ '\n RED:\t' + str(red)\
								+ '\n GREEN:\t' + str(green)\
								+ '\n BLUE:\t' + str(blue))
	else:
		print('Moodlight off')
		print('SPI send: Moodlight off:'\
								+ '\n RED:\t' + str(0)\
								+ '\n GREEN:\t' + str(0)\
								+ '\n BLUE:\t' + str(0))

@socketio.on('delete_alarm')
def delete(id):
	Alarm.query.filter_by(id=int(id)).delete()
	db.session.commit()
	print('Alarm ' + id + ' deleted')

@socketio.on('set_color')
def set_color(color, value):
	global red, green, blue
	if (color == "red"):
		red = value
	elif (color == "green"):
		green = value
	elif (color == "blue"):
		blue = value
	if(moodlight):
		print('SPI send: ' + color + ' updated:'\
									+ '\n RED:\t' + str(red)\
									+ '\n GREEN:\t' + str(green)\
									+ '\n BLUE:\t' + str(blue))
	else:
		print('SPI send: Moodlight off:'\
								+ '\n RED:\t' + str(0)\
								+ '\n GREEN:\t' + str(0)\
								+ '\n BLUE:\t' + str(0))
