from flask_socketio import SocketIO, emit
from app import app, db, alarms, spicom
from app.models import Alarm

socketio = SocketIO(app)

red = 1
green = 1
blue = 1
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
	global moodlight, red, green, blue
	# global state
	moodlight = not moodlight
	if (moodlight):
		spicom.writeCommand([0x32,red,green,blue])
		print('SPI send: Moodlight on:'\
								+ '\n RED:\t' + str(red)\
								+ '\n GREEN:\t' + str(green)\
								+ '\n BLUE:\t' + str(blue))
	else:
		spicom.writeCommand([0x31])
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
	value = int(value)+1
	if(value>250):
		value = 250
	global red, green, blue
	if (color == "red"):
		red = value
	elif (color == "green"):
		green = value
	elif (color == "blue"):
		blue = value
	if(moodlight):
		spicom.writeCommand([0x32,red,green,blue])
		print('SPI send: ' + color + ' updated:'\
									+ '\n RED:\t' + str(red)\
									+ '\n GREEN:\t' + str(green)\
									+ '\n BLUE:\t' + str(blue))
	else:
		spicom.writeCommand([0x31])
		print('SPI send: Moodlight off:'\
								+ '\n RED:\t' + str(0)\
								+ '\n GREEN:\t' + str(0)\
								+ '\n BLUE:\t' + str(0))

@socketio.on('moodlight_off')
def moodlight_off():
	global moodlight, red, green, blue
	red = 1
	green = 1
	blue = 1
	moodlight = 0
	print('Moodlight Off')
	spicom.writeCommand([0x31])

@socketio.on('alarm_off')
def alarm_off():
	print('Alarm Off')
	spicom.writeCommand([0x14])
	spicom.writeCommand([0x13, 0])
	spicom.writeCommand([0x12])

@socketio.on('alarm_on')
def alarm_on():
	print('Alarm On')
	spicom.writeCommand([0x11])
	spicom.writeCommand([0x13, 0])
	spicom.writeCommand([0x15, 0, 10, 1])
