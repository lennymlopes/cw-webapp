from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO

import sched, time, threading
s = sched.scheduler(time.time, time.sleep)


app = Flask(__name__)

# import configurations from config.py
app.config.from_object(Config)

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login
login = LoginManager(app)
login.login_view = 'login'

# bootstrap
bootstrap = Bootstrap(app)

# socketio 
socketio = SocketIO(app)

from app import routes, models, sockets, alarms


def thread_check_for_alarms():
	alarms.check_for_alarms()
	s.enter(60, 1, thread_check_for_alarms)
	s.run()

a=threading.Thread(target=thread_check_for_alarms)
a.daemon = True
a.start()

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=8000)