from App.models import User
from App.models import Competition
from App.database import db


def create_competion(name, category, winner_id, winner, runnerup_id, runnerup, description, results):
    newcomp = Competition(name=name, category=category, winner_id=winner_id, winner=winner, runnerup_id=runnerup_id, runnerup=runnerup, description=description, results = results)
    db.session.add(newcomp)
    db.session.commit()
    return newcomp

#def delete_competition(comp_id):
#   db.session.delete(comp)
 ##   db.session.commit()
   # return True

#def edit_competition(comp_id, name, category, winner, runnerup, description):
 #   comp = Competition.query.get(comp_id)
  #  comp.name = name
   # comp.category = category
#    comp.winner = winner
  #  comp.runnerup = runnerup
  #  comp.description = description
  #  db.session.add(comp)
  #  db.session.commit()
  #  return True