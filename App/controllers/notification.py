from App.models import Notification, Ranking
from sqlalchemy.exc import IntegrityError
from App.controllers import  get_top_20_users_rank
from App.database import db

def generate_notification(userId, message, rank):
    new_Notification = Notification(userId=userId, rank=rank, message=message)
    return new_Notification

def notify(rank, message):
    top_rank = Ranking.query.filter_by(rank=rank).first() # type: ignore
    new_notification = generate_notification(userId=top_rank.profile_id, rank=rank, message=message)
    try:
        db.session.add(new_notification)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    return top_rank


def get_all_notifications():
    return Notification.query.all()

def  get_all_notifications_json():
    get_notfiy = get_all_notifications()
    if not get_notfiy:
        return None
    get_notfiy = [notfi.toJSON() for notfi in get_notfiy]
    return get_notfiy