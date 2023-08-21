import os
import hashlib
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename
import requests
from datetime import datetime
from flask import render_template, redirect, url_for, flash, abort, request, jsonify, session, get_flashed_messages, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from app import db, create_app
from app.forms import RegistrationForm, LoginForm, EditProfileForm, TakeTest, SelectManagerForm, PasswordChangeForm, ContactForm
from datetime import datetime
from werkzeug.exceptions import HTTPException  # import HTTPException instead of abort
from flask import Blueprint
import json
from app.models import User, Company, Results

def save_picture(form_picture, user_email, user_id):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = secure_filename(f'{user_email}-{user_id}{f_ext}')
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_contact_email(name, email, telephone, reason, message):
    url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"

    subject = f"Contact Us - {reason}"

    email_body = f"Name: {name}\n"
    email_body += f"Email: {email}\n"
    email_body += f"Telephone: {telephone}\n\n"
    email_body += f"Message:\n{message}"

    payload = {
        "personalizations": [
            {
                "to": [{"email": "kartik.khosa@gmail.com"}],
                "subject": subject
            }
        ],
        "from": {"email": "kkhosa@seas.upenn.edu"},
        "content": [
            {
                "type": "text/plain",
                "value": email_body
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f10e4ff4cemsh944a4a2544bcab5p1d5686jsne2cd7f364fc9",
        "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 202:
        return 202
    else:
        print("Error details:", response.text)
        return 400


def user_took_test_this_month(user_id):
    """Check if user took test for the current month"""
    last_test = Results.query.filter_by(user_id=user_id).order_by(Results.testDate.desc()).first()

    if not last_test:
        return False

    current_month = datetime.now().month
    current_year = datetime.now().year

    return last_test.testDate.month == current_month and last_test.testDate.year == current_year

def process_test_results(form):
    """Process test form and save results to database"""
    # Questions grouped by section
    section1 = [form.q1, form.q2, form.q3, form.q4, form.q5, form.q6, form.q7]
    section2 = [form.q8, form.q9, form.q10, form.q11, form.q12, form.q13, form.q14]
    section3 = [form.q15, form.q16, form.q17, form.q18, form.q19, form.q20, form.q21, form.q22]

    # Calculate scores for each section
    score1 = sum(int(question.data) for question in section1)
    score2 = sum(int(question.data) for question in section2)
    score3 = sum(int(question.data) for question in section3)
    date = datetime.now()

    # Save scores to database
    try:
        new_test_score = Results(user_id=current_user.id, testDate=date, scoreA=score1, scoreB=score2, scoreC=score3)
        db.session.add(new_test_score)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error while saving test results: {e}")
        db.session.rollback()
        return False

### Reporting/Processing Company Wide Data
def get_burnout_trends():
    # Get the current user's company ID
    company_id = current_user.companyId
    
    # Fetch burnout trends only for the current company
    # For SQLite, use strftime('%m', Results.testDate) to get the month
    last_six_months = db.session.query(
        db.func.strftime('%m', Results.testDate), 
        db.func.avg(Results.scoreA),
        db.func.avg(Results.scoreB),
        db.func.avg(Results.scoreC)
    ).join(User, User.id == Results.user_id).filter(User.companyId == company_id).group_by(db.func.strftime('%m', Results.testDate)).order_by(Results.testDate.desc()).limit(6).all()

    return last_six_months


def get_department_burnout_data():
    # Get the current user's company ID
    company_id = current_user.companyId

    departments = db.session.query(User.department,
        db.func.avg(Results.scoreA),
        db.func.avg(Results.scoreB),
        db.func.avg(Results.scoreC)
    ).join(Results, User.id == Results.user_id).filter(User.companyId == company_id).group_by(User.department).all()

    return departments

def get_team_burnout_data():
    # Get the current user's company ID
    company_id = current_user.companyId

    teams = db.session.query(User.manager_id,
        db.func.avg(Results.scoreA),
        db.func.avg(Results.scoreB),
        db.func.avg(Results.scoreC)
    ).join(Results, User.id == Results.user_id).filter(User.companyId == company_id).group_by(User.manager_id).all()

    return teams

# Function to redirect to appropriate dashboard based on user role_id
def redirect_next_or_dashboard():
    # If there's a next URL provided, redirect there first
    next_page = request.args.get('next')
    if next_page:
        return redirect(next_page)
    
    # Otherwise, determine the dashboard based on the role
    if current_user.role_id == 4 or current_user.role_id == 5:
        return redirect(url_for('main.dashboard'))
    elif current_user.role_id == 3:
        return redirect(url_for('main.hr_overview'))
    elif current_user.role_id == 2:
        return redirect(url_for('main.company_dashboard'))
    else:
        # Fallback to default dashboard or some other page if needed
        return redirect(url_for('main.dashboard'))