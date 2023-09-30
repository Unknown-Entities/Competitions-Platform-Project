from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from .user import User
from .competions import Competition
from App.database import db

class CompetitonUser(User):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'))
    competition = db.relationship('Competition')
    name = db.Column(db.String(120), unique=True)

    def __init__ (self, user_id, competition_id, name):
        self.user_id = user_id
        self.competition_id = competition_id
        self.name = name

    def __repr__(self): # type: ignore
        return f'<Competition: {self.id} | {self.name} | {self.user.username} | {self.competition_id} | {self.competition} | {self.competitions.category}>'

   # def __repr__(self):
       # return{
          #  'id' : self.id,
         #   'name' : self.name,
        #    'competition id' : self.competition.id,
        #    'competition' : self.competition.name,
       #     'category' : self.competition.category,
      #      'winner' : self.competition.winner,
     #       'runner up' : self.competition.runnerup,
    #        'description' : self.competition.description
   #     }


    def save_competition(self, competition_id, name):
        comp = Competition.query.get(competition_id)
        if comp:
            try:
                competition = UserCompetition(self.id, competition_id, name)
                db.session.add(competition)
                db.session.commit()
                return competition
            except Exception:
                db.session.rollback()
                return None
            return None

    def rename_userdescription(self, competition_id, name):
        comp = UserCompetition.query.get(competition_id)
        if comp.user == self:
            comp.name = name
            db.session.add(comp)
            db.session.commit()
            return True
        return None