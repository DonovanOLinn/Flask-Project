from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from uuid import uuid4
from werkzeug.security import generate_password_hash
from datetime import datetime


db = SQLAlchemy()
login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)

class User(db.Model, UserMixin):
        id = db.Column(db.String(40), primary_key=True)
        username = db.Column(db.String(100), nullable=False, unique=True)
        email = db.Column(db.String(100), nullable=False, unique=True)
        password =db.Column(db.String(250), nullable=False)
        first_name = db.Column(db.String(100))
        last_name = db.Column(db.String(100))
        date_created = db.Column(db.DateTime, default=datetime.utcnow())

        def __init__(self, username, email, password, first_name='', last_name=''):
            self.username = username
            self.email = email.lower()
            self.frist_name = first_name.title()
            self.last_name = last_name.title()
            self.id = str(uuid4())
            self.password = generate_password_hash(password)