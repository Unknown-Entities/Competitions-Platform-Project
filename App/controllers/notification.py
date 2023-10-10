from flask import Flask
from App.models import Notification
from flask_socketio import SocketIO
from App.database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
#db = SQLAlchemy(app)


@socketio.on('connect')
def handle_connect():
    print('Client connected')
    
def send_notification(userId, message, read):
    notification = Notification(userId=userId, message=message, read=read)
    db.session.add(notification)
    db.session.commit()
    return socketio.emit('new_notification', {'message': message}, room=userId)
