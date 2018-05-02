from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO

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

from app import routes, models, sockets

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0')