from App.models import User, Ranking, ranking
from App.database import db

def get_rank(id):
    return Ranking.query.get(id)

def calculate_ranking():
    ranks = get_rankings()
    all_ranks = sorted(ranks, key=lambda x: x.points, reverse=True)
    for ranks in all_ranks:
        ranks.rank = all_ranks.index(ranks)
    return all_ranks

def add_ranking(profile_id, name, points, rank): #ranking):
    newrank = Ranking(profile_id=profile_id, name=name, points=points, rank=rank)
    db.session.add(newrank)
    db.session.commit()
    return newrank

def get_rankings():
    return Ranking.query.all()

def get_rankings_json():
    ranks = get_rankings()
    if not ranks:
        return []
    ranks = sorted(ranks, key=lambda rank: rank.points, reverse=True)
    
    send = []
    for rank in ranks:
        add = rank.get_json()
        index = ranks.index(rank) + 1
        if add["Points"] == 0:
            continue

        ranking = get_rank(add["ID"])
        user = User.query.get(add["ID"])
        ranking.rank = index
        user.rank = index

        db.session.add(user)
        db.session.add(ranking)
        db.session.commit()

        send.append(add)
    
    return send
