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

def get_next():
	alarms = get_all()
	now = datetime.datetime.now()
	if not alarms:
		print('no alarms')
		return
	else:
		for alarm in alarms:
			print(str(alarm.hour) + ':' + str(alarm.minute))
