# app/routes.py
print("Routes file loaded!")  # Add this line

from flask import render_template, redirect, url_for, flash, abort, request, jsonify, session, get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from app import db, create_app
from app.forms import RegistrationForm, LoginForm, EditProfileForm
from datetime import datetime
from werkzeug.exceptions import HTTPException  # import HTTPException instead of abort
from flask import Blueprint
from flask import current_app
import json
from app.personalization import save_picture
from app.models import User, Company

login_manager = LoginManager()
login_manager.login_view = 'main.login'
main = Blueprint('main', __name__)

@main.route('/')
def index():
    get_flashed_messages()
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    get_flashed_messages()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Validate the company ID
        try:
            company_id = int(form.companyId.data)
        except ValueError:
            flash('Company ID is not valid. It should be a numeric value.')
            return redirect(url_for('main.register'))

        # Check if the company ID exists
        company = Company.query.get(company_id)
        print(f"Queried company: {company}")  # Debug print
        if company is None:
            print("Company is None, flashing message and redirecting")  # Debug print
            flash('Company ID is not valid. No such company exists.')
            return redirect(url_for('main.register'))

        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Email already registered. Please use a different one or log in.')
            return redirect(url_for('main.register'))

        if form.password.data != form.password_confirm.data:
            flash('Password and confirmation do not match. Please try again.')
            return redirect(url_for('main.register'))

        user = User(email=form.email.data, 
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    companyId=form.companyId.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful.')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))  # Redirect to dashboard if user is already logged in

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email/password combination.')
            return redirect(url_for('main.login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.dashboard'))  # Redirect to dashboard after successful login

    return render_template('login.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    get_flashed_messages()
    user = User.query.filter_by(id=current_user.id).first()
    return render_template('dashboard.html', user=user)


@main.route('/view_profile', methods=['GET', 'POST'])
@login_required
def view_profile():
    form = EditProfileForm(obj=current_user)
    if form.validate_on_submit():
        # Ensure there is a file in the request and that it's not empty
        if 'image' in request.files and request.files['image'].filename != '':
            picture_file = save_picture(form.image.data, current_user.email, current_user.id)
            current_user.image = picture_file
        current_user.email = form.email.data
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.date_of_birth = form.date_of_birth.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.view_profile'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.date_of_birth.data = current_user.date_of_birth
    image = url_for('static', filename='profile_pics/' + current_user.image) if current_user.image else url_for('static', filename='images/profile.jpg')
    return render_template('view_profile.html', title='View Profile', image_file=image, form=form)


@main.route('/test_history')
@login_required
def test_history():
    return render_template('test_history.html')

