#from App.models import User
from App.models import Competition
from App.database import db

def create_competion(id, name, category, description):
    newcomp = Competition(id=id, name=name, category=category,  description=description)
    db.session.add(newcomp)
    db.session.commit()
    return newcomp

def get_competition(id):
    return Competition.query.get(id)

def get_competion_by_name(name):
    return Competition.query.filter_by(name=name).first()

def get_all_competions():
    return Competition.query.all()

def get_all_competions_json():
    comp = Competition.query.all()
    if not comp:
        return []
    comp = [competions.get_json() for competions in comp]
    return comp

def edit_competions(id, name, category, description):
    comp = get_competition(id)
    if comp:
        comp.name = name
        comp.category = category
        comp.description = description
        db.session.add(comp)
        return db.session.commit()
    return None

def update_competions(id, results, winner_id, winner, runnerup_id, runnerup):
    comp = get_competition(id)
    if comp:
        comp.results = results
        comp.winner_id = winner_id
        comp.winner = winner
        comp.runnerup_id = runnerup_id
        comp.runnerup = runnerup
        db.session.add(comp)
        return db.session.commit()
    return None

def delete_competition(id):
    comp = get_competition(id)
  #  if comp:
    db.session.delete(comp)
    db.session.commit()
    return True
