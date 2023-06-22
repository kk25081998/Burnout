# app/routes.py
print("Routes file loaded!")  # Add this line

from flask import render_template, redirect, url_for, flash, abort, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from app import db, create_app
from app.forms import RegistrationForm, LoginForm
from app.models import User
from datetime import datetime
from werkzeug.exceptions import HTTPException  # import HTTPException instead of abort
from flask import Blueprint
from flask import current_app
import json

login_manager = LoginManager()
login_manager.login_view = 'main.login'
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already taken. Please choose a different one.')
            return redirect(url_for('main.register'))

        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Email already registered. Please use a different one or log in.')
            return redirect(url_for('main.register'))

        if form.password.data != form.password_confirm.data:
            flash('Password and confirmation do not match. Please try again.')
            return redirect(url_for('main.register'))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful.')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        session['user_id'] = user.id  # Store the user's id in the session
        return redirect(url_for('main.dashboard'))
    return render_template('login.html', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
