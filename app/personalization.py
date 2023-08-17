import os
import hashlib
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename
import requests

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
