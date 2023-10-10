from flask import Flask, render_template
from App.models import Notification, User, Ranking
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_socketio import emit
from App.database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
db = SQLAlchemy(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

def notify_rank():
    top_20_users = Ranking.get_top_20_users_rank()
    
    for user in top_20_users:
        user_id = user.id
        notification_message = f"Congratulations! your ranking is #{user.rank}."
        notification_type = "info"
        send_notification(user_id, notification_message, notification_type)


def send_notification(userId, user_id, message, notification_type):
    notification = Notification(userId=userId, user_id=user_id, message=message, notification_type = notification_type, read=False)
    db.session.add(notification)
    db.session.commit()

    # Broadcast the notification to the user
    emit('new_notification', {'message': message, 'type': notification_type}, room=user_id)

notify_rank()

if __name__ == '_main_':
    socketio.run(app)