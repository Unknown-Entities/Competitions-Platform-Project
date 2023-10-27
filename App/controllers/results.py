#from App.models import User
from App.models import Competition, Results
from App.database import db
from .user import get_user
from .competions import get_competition
from .ranking import get_rank

def gather_results(id):
    getresults = Results.query.filter_by(competitionId=id).all()
    getresults = sorted(getresults, key=lambda getresult: getresult.score, reverse=True)
    results = [getresult.get_result_json(getresults.index(getresult)) for getresult in getresults]

    competition = Competition.query.filter_by(id=id).first()
    if competition:
        if not results[1]['Name']:
            competition.runnerup = "None"
        if results[1]['Name']:
            competition.runnerup = results[1]['Name']
        if not results[0]['Name']:
            competition.winner = "None"
        if results[0]['Name']:
            competition.winner = results[0]['Name']
        db.session.add(competition)
        db.session.commit()
    return results

def add_results(userId, competitionId, score):
    user = get_user(userId)
    competition = get_competition(competitionId)
    result_match = check_duplicate(userId, competitionId)
    if user and competition:
        if result_match == False:
            newresult = Results(userId=userId, competitionId=competitionId, score=score)
            ranking = get_rank(userId)
            ranking.points += int(score)
            db.session.add(newresult)
            db.session.add(ranking)
            db.session.commit()
            return newresult
        return None
    return None

def check_duplicate(userId, competitionId):
    result = Results.query.filter_by(competitionId=competitionId, userId=userId).first()
    if result:
        return True
    return False

def check_competitions(userId):
    competitions = Competition.query.all()
    results = []
    for competition in competitions:
        check = Results.query.filter_by(userId=userId, competitionId=competition.id).first()
        if check:
            add = get_competition(competition.id)
            results.append(add)
    results = [result.get_json() for result in results]
    return results