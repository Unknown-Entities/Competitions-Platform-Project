from .user import User
from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    winner = db.Column(db.String(255), nullable=False)
    runnerup_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    runnerup = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    results = db.Column(db.Integer, nullable=False)

    def __init__(self, name, category, winner_id, winner, runnerup_id, runnerup, description, results):
        self.name = name
        self.category = category
        self.winner_id = winner_id
        self.winner = winner
        self.runnerup_id = runnerup_id
        self.runnerup = runnerup
        self.description = description
        self.results = results

    def get_json(self):
        return{
            'id': self.id,
            'name' : self.name,
            'category' : self.category,
            #'winner id' : self.winner_id,
            'winner' : self.winner,
            #'runner up id' : self.runnerup_id,
            'runner up' : self.runnerup,
            'description': self.description,
            #'results': self.results
        }