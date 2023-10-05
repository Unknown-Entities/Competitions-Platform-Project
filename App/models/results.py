from .user import User
from .competions import Competition
from App.database import db


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('user.id'))
    competitionId = db.Column(db.Integer,db.ForeignKey('competition.id'))
    score = db.Column(db.Integer, nullable=False)
    #timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, userId, competitionId, score):
            self.userId = userId
            self.competitionId = competitionId
            self.score = score
            #self.timestamp = timestamp

    def __repr__(self):
        return f'<User {self.id} {self.username} {self.email}>'

    def get_json(self):
        return{
            'userId': self.userId,
            'competitionId': self.competitionId,
            'score': self.score,
            #'timestamp': self.timestamp
        }
    
    def get_result_json(self, index):
        username = User.query.get(self.userId)
        index = index + 1
        return{
            'Name': username.username,
            'Place': index,
            'Score': self.score,
            #'timestamp': self.timestamp
        }