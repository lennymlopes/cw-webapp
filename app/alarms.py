from app import db
import datetime
from app.models import Alarm

class time:
    def __init__(self):
        self.hour = None
        self.minute = None

def get_all():

	alarms = Alarm.query.all()
	# now = datetime.datetime.now()
	# for alarm in alarms:
		# print(alarm.hour + ':' + alarm.minute)
	return alarms

def check_for_alarms():
	alarms = get_all()
	number = 0
	today = datetime.datetime.today().weekday()
	if(today == 0):
		for alarm in alarms:
			if (alarm.monday):
				return True
			else:
				return False
	if(today == 6):
		for alarm in alarms:
			if(alarm.sunday):
				number += 1
		
		if(number):
			print('Today are ' + str(number) + ' alarms')
			return True
		else:
			print('No alarms today')
			return False


def get_next():
	alarms = get_all()
	now = datetime.datetime.now()
	now = now.hour*3600+now.minute*60
	alarm_list = []
	print(datetime.datetime.today().weekday())
	if not alarms:
		print('no alarms')
		return
	else:
		for alarm in alarms:
			alarm_list.append(alarm.time)
	alarm_list.sort()
	if max(alarm_list) < now:	# if next alarm is on new day
		print('Next alarm: ' + str(datetime.timedelta(seconds=min(alarm_list))))
	else:
		for alarm in alarm_list:
			if now < alarm:
				print('Next alarm: ' + str(datetime.timedelta(seconds=alarm)))