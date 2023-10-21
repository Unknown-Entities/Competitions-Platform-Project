from App.database import db


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    rank = db.Column(db.Integer, db.ForeignKey('ranking.id'))
    message = db.Column(db.String, nullable=False)
    read = db.Column(db.Boolean, default=False)
    

    def __init__(self, userId, message, rank):
        self.userId = userId
        self.rank = rank
        self.message = message
        self.read ="unread"

    def get_json(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'message': self.message,
            'rank': self.rank,
            'read': self.read
        }
