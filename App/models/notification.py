from App.database import db


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Boolean, default=False)
    

    def __init__(self, userId, message, read):
        self.userId = userId
        self.message = message
        self.read = read

    def get_json(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'message': self.message,
            'read': self.read
        }
