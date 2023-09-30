from App.models import User
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def get_rank(id):
    user = get_user(id)
    return user.rank

def populate_ranks(users):
    rankings = [User.get_rank() for user in users]
    return rankings

def calculate_ranking():
    users = get_all_users()

    scores = populate_ranks(users)
    all_scores = sorted(set(scores), reverse=True)
    ranks = [scores.index(x) + 1 for x in scores]
    return ranks
    