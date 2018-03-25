from app import app

from app.models import User, Alarm

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Alarm': Alarm}