from App.models import User, Ranking
from App.database import db
from .user import get_all_users, get_all_users_json, get_user

def get_rank(profile_id):
    return Ranking.query.get(profile_id)

def calculate_ranking():
    ranks = get_rankings()
    all_ranks = sorted(ranks, key=lambda x: x.points, reverse=True)
    for ranks in all_ranks:
        ranks.rank = all_ranks.index(ranks)
    return all_ranks

def add_ranking(ranking):
    newrank = Ranking(id=id, profile_id=profile_id, name=name, points=points, rank=rank)
    db.session.add(newrank)
    db.session.commit()
    return newrank

def get_rankings():
    return Ranking.query.all()

def get_rankings_json():
    ranks = calculate_ranking()
    if not ranks:
        return []
    return [ranks.toJSON() for rank in ranks]