from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(64), nullable=False)  
    lastname = db.Column(db.String(64), nullable=False)  
    image = db.Column(db.String(128), nullable=True)  
    date_of_birth = db.Column(db.String(64), nullable=True)  # changed from db.Date to db.String
    companyId = db.Column(db.Integer, db.ForeignKey('company.id')) 
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    results = db.relationship('Results', backref='user', lazy='dynamic')
    subordinates = db.relationship('User', backref=db.backref('manager', remote_side=[id]), lazy='dynamic')
    first_login = db.Column(db.Boolean, default=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return f'<User {self.firstname} {self.lastname}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128), nullable=True)
    size = db.Column(db.Integer, nullable=True)
    users = db.relationship('User', backref='company', lazy='dynamic') 

    def __repr__(self):
        return f'<Company {self.name}>'


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    testDate = db.Column(db.Date, nullable=False)
    scoreA = db.Column(db.Integer, nullable=False)
    scoreB = db.Column(db.Integer, nullable=False)
    scoreC = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Results {self.id}>'

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
