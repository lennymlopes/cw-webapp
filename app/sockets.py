from flask_socketio import SocketIO, emit
from app import app

socketio = SocketIO(app)

@socketio.on('update')
def update_db(parameter):
	print('Button ' + parameter)