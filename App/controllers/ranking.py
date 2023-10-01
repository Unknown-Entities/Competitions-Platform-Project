from App.models import User
from App.database import db

def get_rank():
    return User.rank

def populate_ranks(users):
    rankings = [User.get_rank() for user in users]
    return rankings

def calculate_ranking():
    users = get_all_users()

    scores = populate_ranks(users)
    all_scores = sorted(set(scores), reverse=True)
    ranks = [scores.index(x) + 1 for x in scores]
    return ranks

def add_ranking(self, ranking):
    self.rankings_list.append(ranking)

def get_rankings(self):
    return self.rankings_list