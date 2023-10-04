#from App.models import User
from App.models import Competition, Results
from App.database import db

def gather_results(id):
    results = [Results.query.filter_by(competitionId=id)]
    sorted_results = sorted(results, key=lambda result: result.score)
    sorted_results = [results.get_json() for sorted_result in sorted_results]
    return sorted_results

def add_results():
    newresult = Results(userId=userId, competitionId=competitionId, score=score)
    db.session.add(newresult)
    db.session.commit()
    return newcomp