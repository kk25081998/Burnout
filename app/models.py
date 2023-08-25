from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from datetime import datetime
from sqlalchemy.orm import aliased

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
    department = db.Column(db.String(128), nullable=True)
    title = db.Column(db.String(128), nullable=True)
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
    industry = db.Column(db.String(128), nullable=False) 
    frequency = db.Column(db.String(64), nullable=True)
    image = db.Column(db.String(128), nullable=True)  
    
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


role_permissions = db.Table('role_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    permissions = db.relationship('Permission', secondary=role_permissions, backref=db.backref('roles', lazy='dynamic'))


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)  # A brief description of what this permission allows

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id')) 
    date_submitted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)  # Text field to allow longer feedback
    status = db.Column(db.String(64), default="Pending")  # Useful to track feedback status

    def __repr__(self):
        return f'<Feedback {self.id} for Company {self.company_id}>'

class Resources(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    link = db.Column(db.String(500), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Resource('{self.title}', '{self.category}')"