from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from .user import User
from .competion_User import CompetitonUser
from App.database import db


class Competition(CompetitonUser):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    winner = db.Column(db.String(255), nullable=False)
    runnerup = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def get_json(self):
        return{
            'competition_id': self.id,
            'name' : self.name,
            'category' : self.category,
            'winner' : self.winner,
            'runner up' : self.runnerup,
            'description': self.description
        }

    def delete_competition(comp_id):
        comp = Competition.query.get(comp_id)
        db.session.delete(comp)
        db.session.commit()
        return True

    def edit_competition(comp_id, name, category, winner, runnerup, description):
        comp = Competition.query.get(comp_id)
        comp.name = name
        comp.category = category
        comp.winner = winner
        comp.runnerup = runnerup
        comp.description = description
        db.session.add(comp)
        db.session.commit()
        return True
    
