from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wsgi import app

db = SQLAlchemy(app)

def get_migrate(app):
    return Migrate(app, db)

def create_db():
    db.create_all()
    
def init_db(app):
    db.init_app(app)
