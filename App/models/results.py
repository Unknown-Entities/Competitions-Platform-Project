from App.database import db
from datetime import datetime


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('user.id'))
    competionId = db.Column(db.Integer,db.ForeignKey('competions.id'))
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    competition = db.relationship('Competition', backref=db.backref('results', lazy='joined'))
    rank = db.relationship('Ranking', backref=db.backref('results', lazy='joined'))


    def __init__(self, userId, competionId, score, timestamp):
            self.id = id,
            self.userId = userId
            self.competionId = competionId
            self.score = score
            self.timestamp = timestamp

    def __repr__(self):
        return f'<User {self.id} {self.score} {self.rank}>'

    def get_json(self):
        return{
            'id': self.id,
            'userId': self.userId,
            'competionId': self.competionId,
            'score': self.score,
            'timestamp': self.timestamp
        }