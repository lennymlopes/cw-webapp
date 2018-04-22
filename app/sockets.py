from app import socketio

@socketio.on('update')
def update_db(parameter):
	print('Button ' + parameter)