from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object('config.Config')
    app.config['DEBUG'] = True

    db.init_app(app)  # Initialize the db object
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.routes import main

    return app