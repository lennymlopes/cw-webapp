from flask_socketio import SocketIO, emit
from app import app

socketio = SocketIO(app)

@socketio.on('update')
def update(parameter, data):
	print('Updated ' + parameter + ': ' + data)