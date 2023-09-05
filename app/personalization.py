import os
import hashlib
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename
import requests
from datetime import datetime
from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    abort,
    request,
    jsonify,
    session,
    get_flashed_messages,
    send_from_directory,
)
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
    LoginManager,
)
from app import db, create_app
from app.forms import (
    LoginForm,
    EditProfileForm,
    TakeTest,
    SelectManagerForm,
    PasswordChangeForm,
    ContactForm,
)
from datetime import datetime
from werkzeug.exceptions import HTTPException  # import HTTPException instead of abort
from flask import Blueprint
import json
from app.models import User, Company, Results
from sqlalchemy import extract, func, distinct, cast, Integer, text


def save_picture(form_picture, user_email, user_id):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = secure_filename(f"{user_email}-{user_id}{f_ext}")
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_fn
    )

    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def save_company_logo(form_logo):
    _, f_ext = os.path.splitext(form_logo.filename)
    logo_filename = secure_filename(f"company-{current_user.company.id}{f_ext}")
    logo_path = os.path.join(
        current_app.root_path, "static/company_logo", logo_filename
    )

    output_size = (300, 300)
    i = Image.open(form_logo)
    i.thumbnail(output_size)
    i.save(logo_path)

    return logo_filename


def send_contact_email(name, email, telephone, reason, message):
    url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"

    subject = f"Contact Us - {reason}"

    email_body = f"Name: {name}\n"
    email_body += f"Email: {email}\n"
    email_body += f"Telephone: {telephone}\n\n"
    email_body += f"Message:\n{message}"

    payload = {
        "personalizations": [
            {"to": [{"email": "kartik.khosa@gmail.com"}], "subject": subject}
        ],
        "from": {"email": "kkhosa@seas.upenn.edu"},
        "content": [{"type": "text/plain", "value": email_body}],
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f10e4ff4cemsh944a4a2544bcab5p1d5686jsne2cd7f364fc9",
        "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com",
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 202:
        return 202
    else:
        print("Error details:", response.text)
        return 400


def user_took_test_this_month(user_id):
    """Check if user took test for the current month"""
    last_test = (
        Results.query.filter_by(user_id=user_id)
        .order_by(Results.testDate.desc())
        .first()
    )

    if not last_test:
        return False

    current_month = datetime.now().month
    current_year = datetime.now().year

    return (last_test.testDate.year > current_year) or (
        last_test.testDate.year == current_year
        and last_test.testDate.month >= current_month
    )


def process_test_results(form):
    """Process test form and save results to database"""
    # Questions grouped by section
    section1 = [form.q1, form.q2, form.q3, form.q4, form.q5, form.q6, form.q7]
    section2 = [form.q8, form.q9, form.q10, form.q11, form.q12, form.q13, form.q14]
    section3 = [
        form.q15,
        form.q16,
        form.q17,
        form.q18,
        form.q19,
        form.q20,
        form.q21,
        form.q22,
    ]

    # Calculate scores for each section
    score1 = sum(int(question.data) for question in section1)
    score2 = sum(int(question.data) for question in section2)
    score3 = sum(int(question.data) for question in section3)
    date = datetime.now()

    # Save scores to database
    try:
        new_test_score = Results(
            user_id=current_user.id,
            testDate=date,
            scoreA=score1,
            scoreB=score2,
            scoreC=score3,
        )
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

    # Extract month and year from testDate for grouping and ordering
    extracted_month = db.func.extract("month", Results.testDate).label("month")
    extracted_year = db.func.extract("year", Results.testDate).label("year")

    # Fetch burnout trends only for the current company
    last_six_months = (
        db.session.query(
            extracted_month,
            extracted_year,
            db.func.avg(Results.scoreA),
            db.func.avg(Results.scoreB),
            db.func.avg(Results.scoreC),
        )
        .join(User, User.id == Results.user_id)
        .filter(User.companyId == company_id)
        .group_by(extracted_month, extracted_year)
        .order_by(extracted_year.desc(), extracted_month.desc())
        .limit(6)
        .all()
    )

    return last_six_months


def get_department_burnout_data(company_id):
    department_monthly_scores = (
        db.session.query(
            User.department,
            extract("year", Results.testDate).label("year"),
            extract("month", Results.testDate).label("month"),
            func.round(
                100
                * func.avg(Results.scoreA + Results.scoreB + (48 - Results.scoreC))
                / 132
            ).label("avg_burnout"),
        )
        .join(Results, User.id == Results.user_id)
        .filter(User.companyId == company_id)
        .group_by(User.department, "year", "month")
        .order_by(
            extract("year", Results.testDate).desc(), extract("month", Results.testDate)
        )
        .all()
    )

    result_dict = {}
    for dep, year, month, avg in department_monthly_scores:
        month_str = str(int(month)).zfill(
            2
        )  # Convert month to string and pad with zeros
        month_year = f"{year}-{month_str}"
        if dep not in result_dict:
            result_dict[dep] = {}
        result_dict[dep][month_year] = avg

    return result_dict


def get_team_burnout_data(company_id):
    manager_monthly_scores = (
        db.session.query(
            User.manager_id,
            extract("year", Results.testDate).label("year"),
            extract("month", Results.testDate).label("month"),
            func.round(
                100
                * func.avg(Results.scoreA + Results.scoreB + (48 - Results.scoreC))
                / 132
            ).label("avg_burnout"),
        )
        .join(Results, User.id == Results.user_id)
        .filter(User.companyId == company_id)
        .group_by(User.manager_id, "year", "month")
        .order_by(text("year DESC, month DESC"))
        .all()
    )

    result_dict = {}
    for manager, year, month, avg in manager_monthly_scores:
        month_str = str(int(month)).zfill(
            2
        )  # Convert month to string and pad with zeros
        month_year = f"{year}-{month_str}"
        if manager not in result_dict:
            result_dict[manager] = {}
        result_dict[manager][month_year] = avg

    return result_dict


# Function to redirect to appropriate dashboard based on user role_id
def redirect_next_or_dashboard():
    # If there's a next URL provided, redirect there first
    next_page = request.args.get("next")
    if next_page:
        return redirect(next_page)

    # Otherwise, determine the dashboard based on the role
    if current_user.role_id == 4 or current_user.role_id == 5:
        return redirect(url_for("main.dashboard"))
    elif current_user.role_id == 3:
        return redirect(url_for("main.hr_overview"))
    elif current_user.role_id == 2:
        return redirect(url_for("main.company_dashboard"))
    else:
        # Fallback to default dashboard or some other page if needed
        return redirect(url_for("main.dashboard"))


def create_departments(company_id):
    distinct_department_names = (
        db.session.query(User.department)
        .filter_by(companyId=company_id)
        .distinct()
        .all()
    )
    department_names = [row[0] for row in distinct_department_names]
    return department_names
