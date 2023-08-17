# app/routes.py
from flask import render_template, redirect, url_for, flash, abort, request, jsonify, session, get_flashed_messages, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from app import db, create_app
from app.forms import RegistrationForm, LoginForm, EditProfileForm, TakeTest, SelectManagerForm, PasswordChangeForm, ContactForm
from datetime import datetime
from werkzeug.exceptions import HTTPException  # import HTTPException instead of abort
from flask import Blueprint
from flask import current_app
import json
from app.personalization import save_picture, send_contact_email, user_took_test_this_month, process_test_results
from app.models import User, Company, Results
from datetime import datetime

login_manager = LoginManager()
login_manager.login_view = 'main.login'
main = Blueprint('main', __name__)

@main.route('/')
def index():
    get_flashed_messages()
    return render_template('index.html')


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

        # Check if it's the user's first login
        if user.first_login:
            return redirect(url_for('main.change_password'))  # Redirect to password change form on first login

        return redirect(url_for('main.dashboard'))  # Redirect to dashboard after successful login

    return render_template('login.html', form=form)

@main.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = PasswordChangeForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            flash('Incorrect old password')
            return redirect(url_for('main.change_password'))

        current_user.set_password(form.new_password.data)
        current_user.first_login = False  # Set first_login attribute to False
        db.session.commit()
        flash('Your password has been updated.')
        return redirect(url_for('main.dashboard'))
    return render_template('change_password.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    get_flashed_messages()
    user = User.query.filter_by(id=current_user.id).first()
    last_score = Results.query.filter_by(user_id=current_user.id).order_by(Results.testDate.desc()).first()
    last_three_scores = Results.query.filter_by(user_id=current_user.id).order_by(Results.testDate.desc()).limit(3).all()
    
    # Fetch all results for the user to display in the chart
    all_results = Results.query.filter_by(user_id=current_user.id).order_by(Results.testDate.asc()).all()
    
    current_month = datetime.now().month
    last_month = (current_month - 1) % 12 or 12
    two_months_ago = (current_month - 2) % 12 or 12
    
    scores_dict = {score.testDate.month: score for score in last_three_scores}

    return render_template('dashboard.html', user=user, last_score=last_score, last_three_scores=last_three_scores, current_month=current_month, scores_dict=scores_dict, last_month=last_month, two_months_ago=two_months_ago)
    
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

@main.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    form = TakeTest()
    
    # Check if the user has taken the test in the current month
    if user_took_test_this_month(current_user.id):
        next_month = datetime(datetime.now().year, datetime.now().month % 12 + 1, 1)  # First day of next month
        flash(f'You can only take the burnout test once per calendar month. Please come back on {next_month.strftime("%B %d, %Y")} to take the test again.', 'warning')
        return render_template('test_not_eligible.html', title='test', form=form, next_eligible_date=next_month)

    if form.validate_on_submit():
        # Process the form and save the results
        if process_test_results(form):
            flash('Your test has been successfully submitted!')
            return redirect(url_for('main.test_history'))

    # Questions grouped by section
    section1 = [form.q1, form.q2, form.q3, form.q4, form.q5, form.q6, form.q7]
    section2 = [form.q8, form.q9, form.q10, form.q11, form.q12, form.q13, form.q14]
    section3 = [form.q15, form.q16, form.q17, form.q18, form.q19, form.q20, form.q21, form.q22]

    return render_template('test.html', title='test', form=form, section1=section1, section2=section2, section3=section3)

@main.route('/test_history', methods=['GET'])
@login_required
def test_history():
    # Query the database for the user's results
    results = Results.query.filter_by(user_id=current_user.id).order_by(Results.testDate.desc()).all()

    return render_template('test_history.html', title='Test History', results=results)

@main.route('/team_test_history', methods=['GET'])
@login_required
def team_test_history():
    # Query the database for the current user's subordinates' results
    subordinates_results = (
        Results.query
        .join(User, User.id == Results.user_id)
        .filter(User.manager_id == current_user.id)
        .order_by(Results.testDate.desc())
    )

    return render_template(
        'team_test_history.html', 
        title='Team Test History', 
        subordinates_results=subordinates_results
    )

@main.route('/select_manager', methods=['GET', 'POST'])
@login_required
def select_manager():
    form = SelectManagerForm()
    form.manager.choices = [(0, 'None')] + [(u.id, f'{u.firstname} {u.lastname}') for u in User.query.filter_by(companyId=current_user.companyId).all() if u.id != current_user.id]
    if form.validate_on_submit():
        current_user.manager_id = form.manager.data
        db.session.commit()
        flash('Your manager has been selected.')
        return redirect(url_for('main.index'))  # redirect to the index page or any other page after manager selection
    return render_template('select_manager.html', form=form)

@main.before_request
def before_request():
    if current_user.is_authenticated and current_user.manager_id is None and request.endpoint not in ['main.select_manager', 'main.logout']:
        return redirect(url_for('main.select_manager'))

@main.route('/resources', methods=['GET'])
# @login_required
def resources():
    return render_template('resources.html', title='Wellness Hub')


@main.route('/pricing', methods=['GET'])
def pricing():
    return render_template('pricing.html', title='Pricing')


@main.route('/company', methods=['GET'])
def company():
    return render_template('company.html')

@main.route('/contactus', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        telephone = form.telephone.data
        reason = form.reason.data
        message = form.message.data

        formatted_message = f"Name: {name}\nEmail: {email}\nTelephone: {telephone}\n\nMessage:\n{message}"
        
        response_code = send_contact_email(name, email, telephone, reason, formatted_message)
        
        if response_code == 202:
            # Clear the form fields by rendering it with empty data
            form.name.data = ''
            form.email.data = ''
            form.telephone.data = ''
            form.reason.data = 'Select Reason'  # Reset the dropdown to the default option
            form.message.data = ''
            success_message = "Your message has been sent successfully. Thank you!"
            error_message = None
        else:
            success_message = None
            error_message = "Oops! Something went wrong while sending the message. Please try again later."

        return render_template('contactus.html', title='Contact Us', form=form, success_message=success_message, error_message=error_message)

    return render_template('contactus.html', title='Contact Us', form=form, success_message=None, error_message=None)





@main.route('/termsofservice', methods=['GET'])
def tos():
    return render_template('termsofservice.html')

@main.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    return render_template('privacy-policy.html')

# Route to serve the favicon.ico file
@main.route('/favicon.ico')
def favicon():
    user_agent = request.headers.get('User-Agent', '').lower()

    if 'android' in user_agent:
        return send_from_directory(
            current_app.root_path,
            'static/images/android-chrome-192x192.png',
            mimetype='image/png'
        )
    elif 'apple' in user_agent:
        return send_from_directory(
            current_app.root_path,
            'static/images/apple-touch-icon.png',
            mimetype='image/png'
        )
    else:
        return send_from_directory(
            current_app.root_path,
            'static/images/favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )



# @main.route('/test', methods=['GET', 'POST'])
# @login_required
# def test():
#     form = TakeTest()
    
#     # Fetch the most recent test date for the user
#     last_test = Results.query.filter_by(user_id=current_user.id).order_by(Results.testDate.desc()).first()

#     # Check if the user has taken the test in the current month
#     if last_test and last_test.testDate.month == datetime.now().month and last_test.testDate.year == datetime.now().year:
#         next_month = datetime(datetime.now().year, datetime.now().month % 12 + 1, 1)  # First day of next month
#         flash(f'You can only take the burnout test once per calendar month. Please come back on {next_month.strftime("%B %d, %Y")} to take the test again.', 'warning')
#         return render_template('test.html', title='test', form=form, next_eligible_date=next_month)

#     # Questions grouped by section
#     section1 = [form.q1, form.q2, form.q3, form.q4, form.q5, form.q6, form.q7]
#     section2 = [form.q8, form.q9, form.q10, form.q11, form.q12, form.q13, form.q14]
#     section3 = [form.q15, form.q16, form.q17, form.q18, form.q19, form.q20, form.q21, form.q22]

#     print("Form data: ", form.data)
#     print("Form errors: ", form.errors)

#     if form.validate_on_submit():
#         #debug
#         print([question.data for question in section1])
#         print([question.data for question in section2])
#         print([question.data for question in section3])

#         # Calculate scores for each section
#         score1 = sum(int(question.data) for question in section1)
#         score2 = sum(int(question.data) for question in section2)
#         score3 = sum(int(question.data) for question in section3)
#         date = datetime.datetime.now()

#         # Save scores to database
#         try:
#             new_test_score = Results(user_id=current_user.id, testDate=date, scoreA=score1, scoreB=score2, scoreC=score3, )
#             db.session.add(new_test_score)
#             db.session.commit()
#         except Exception as e:
#             print(f"Error while saving test results: {e}")
#             db.session.rollback()


#         flash('Your test has been successfully submitted!')
#         return redirect(url_for('main.test_history'))
    
#     return render_template('test.html', title='test', form=form, section1=section1, section2=section2, section3=section3)

# @main.route('/register', methods=['GET', 'POST'])
# def register():
#     get_flashed_messages()
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index'))

#     form = RegistrationForm()
#     if form.validate_on_submit():
#         # Validate the company ID
#         try:
#             company_id = int(form.companyId.data)
#         except ValueError:
#             flash('Company ID is not valid. It should be a numeric value.')
#             return redirect(url_for('main.register'))

#         # Check if the company ID exists
#         company = Company.query.get(company_id)
#         print(f"Queried company: {company}")  # Debug print
#         if company is None:
#             print("Company is None, flashing message and redirecting")  # Debug print
#             flash('Company ID is not valid. No such company exists.')
#             return redirect(url_for('main.register'))

#         existing_email = User.query.filter_by(email=form.email.data).first()
#         if existing_email:
#             flash('Email already registered. Please use a different one or log in.')
#             return redirect(url_for('main.register'))

#         if form.password.data != form.password_confirm.data:
#             flash('Password and confirmation do not match. Please try again.')
#             return redirect(url_for('main.register'))

#         user = User(email=form.email.data, 
#                     firstname=form.firstname.data,
#                     lastname=form.lastname.data,
#                     companyId=form.companyId.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Registration successful.')
#         return redirect(url_for('main.select_manager'))

#     return render_template('register.html', form=form)