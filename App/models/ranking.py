from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin

class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    def __init__(self, profile_id, name, points, rank):
        self.profile_id = profile_id
        self.name = name
        self.points = points
        self.rank = rank

    def get_json(self):
        return{
            'ID': self.profile_id,
            'Name': self.name,
            'Points': self.points,
            'Rank': self.rank
        }