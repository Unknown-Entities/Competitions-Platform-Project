from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    rank = db.Column(db.Integer, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False)
    #competition = db.relationship('Competition', backref=db.backref('user', lazy='joined'))

    def __init__(self, username, password, email, rank, is_admin):
        self.username = username
        self.set_password(password)
        self.email = email
        self.rank = rank
        self.is_admin = is_admin
    
    def __repr__(self):
        return f'<User {self.id} {self.username}>'

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'rank': self.rank
        }