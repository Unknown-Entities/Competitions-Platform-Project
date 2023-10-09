from flask import Flask, render_template
from App.models import Notification, User, Ranking
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
db = SQLAlchemy(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

def send_notification(userId, message, read):
    notification = Notification(userId=userId, message=message, read=read)
    db.session.add(notification)
    db.session.commit()

    # Broadcast the notification to the user
    emit('new_notification', {'message': message}, room=userId)