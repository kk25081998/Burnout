from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Use sqlite for simplicity
db = SQLAlchemy(app)
login = LoginManager(app)

from app.models import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
