from app import db, spicom
import datetime
from app.models import Alarm
from enum import Enum
import pytz

class time:
    def __init__(self):
        self.hour = None
        self.minute = None


def check_for_alarms():
	
	today = datetime.datetime.today().weekday()
	tz = pytz.timezone('Europe/Zurich')
	now = datetime.datetime.now(tz)
	now = now.hour*3600+now.minute*60
	alarms = Alarm.query.all()
	alarm_list = []

	# monday
	if(today==0):
		for alarm in alarms:
			if(alarm.monday and alarm.active):
				alarm_list.append(alarm.time)
	#tuesday
	elif(today==1):
		for alarm in alarms:
			if(alarm.tuesday and alarm.active):
				alarm_list.append(alarm.time)
	#wednesday
	elif(today==2):
		for alarm in alarms:
			if(alarm.wednesday and alarm.active):
				alarm_list.append(alarm.time)
	#thursday
	elif(today==3):
		for alarm in alarms:
			if(alarm.thursday and alarm.active):
				alarm_list.append(alarm.time)
	#friday
	elif(today==4):
		for alarm in alarms:
			if(alarm.friday and alarm.active):
				alarm_list.append(alarm.time)
	#friday
	elif(today==5):
		for alarm in alarms:
			if(alarm.friday and alarm.active):
				alarm_list.append(alarm.time)
	#sunday
	if(today==6):
		print('its sunday')
		for alarm in alarms:
			if(alarm.sunday and alarm.active):
				alarm_list.append(alarm.time)
	alarm_list.sort()
	print(alarm_list)

	if max(alarm_list) < now:	# if next alarm is on new day
		print('Next alarm: ' + str(datetime.timedelta(seconds=min(alarm_list))))
		print('Alarm on new Day')
		return(False)
	else:
		print(now, alarm.time)
		for alarm in alarm_list:
			if now < alarm:
				print('Next alarm: ' + str(datetime.timedelta(seconds=alarm)))
				return datetime.timedelta(seconds=alarm)
			elif now == alarm:
				print('SPI send: start alarm')
				spicom.writeCommand([0x11])
				spicom.writeCommand([0x13, 0])
				spicom.writeCommand([0x15, 0, 10, 1])



