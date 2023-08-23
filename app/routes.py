# app/routes.py
from flask import render_template, redirect, url_for, flash, abort, request, jsonify, session, get_flashed_messages, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from app import db, create_app
from app.forms import RegistrationForm, LoginForm, EditProfileForm, TakeTest, SelectManagerForm, PasswordChangeForm, ContactForm, UnifiedUserForm, FeedbackForm, CompanySettingsForm
from datetime import datetime
from werkzeug.exceptions import HTTPException  # import HTTPException instead of abort
from flask import Blueprint
from flask import current_app
import json
from app.personalization import save_picture, send_contact_email, user_took_test_this_month, process_test_results, get_burnout_trends, get_department_burnout_data, get_team_burnout_data, save_company_logo, redirect_next_or_dashboard
from app.models import User, Company, Results, Feedback
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import extract, func, distinct, cast, Integer

login_manager = LoginManager()
login_manager.login_view = 'main.login'
main = Blueprint('main', __name__)

@main.route('/')
def index():
    get_flashed_messages()
    return render_template('intro.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect_next_or_dashboard()  # Redirect to appropriate dashboard if user is already logged in

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

        return redirect_next_or_dashboard()  # Redirect to appropriate dashboard after successful login

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
        return redirect_next_or_dashboard()  # Redirect to appropriate dashboard after successful login
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
    today_date = datetime.now().date()  # Get the current date without time.
    # Get the first day of the current month.
    first_day_of_current_month = today_date.replace(day=1)
    last_day_of_last_month = first_day_of_current_month - timedelta(days=1)

    last_score = Results.query.filter_by(user_id=current_user.id).filter(Results.testDate <= today_date).order_by(Results.testDate.desc()).first()
    last_three_scores = (Results.query
                    .filter(Results.user_id == current_user.id)
                    .filter(Results.testDate <= last_day_of_last_month)  # Exclude scores with future dates.
                    .order_by(Results.testDate.desc())
                    .limit(3)
                    .all())

    # Fetch all results for the user to display in the chart
    all_results = Results.query.filter_by(user_id=current_user.id).order_by(Results.testDate.asc()).all()

    current_month = datetime.now().month
    last_month = (current_month - 1) % 12 or 12
    two_months_ago = (current_month - 2) % 12 or 12
    three_months_ago = (current_month - 3) % 12 or 12

    current_year = datetime.now().year
    prev_year = current_year - 1


    scores_dict = {}

    for score in last_three_scores:
        scores_dict[score.testDate.month] = score

    print(scores_dict)
    return render_template('dashboard.html', user=user, last_score=last_score, current_month=current_month, scores_dict=scores_dict, last_month=last_month, two_months_ago=two_months_ago, three_months_ago = three_months_ago, current_year=current_year, prev_year=prev_year)


@main.route('/view_profile', methods=['GET', 'POST'])
@login_required
def view_profile():
    form = EditProfileForm(obj=current_user)
    message = None
    message_type = None
    image = url_for('static', filename='profile_pics/' + current_user.image) if current_user.image else url_for('static', filename='images/profile.jpg')

    if request.method == 'GET':
        form.email.data = current_user.email
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.date_of_birth.data = current_user.date_of_birth
        return render_template('view_profile.html', title='View Profile', image_file=image, form=form, message='', message_type='')

    if form.validate_on_submit():
        try:
            # Ensure there is a file in the request and that it's not empty
            if 'image' in request.files and request.files['image'].filename != '':
                picture_file = save_picture(form.image.data, current_user.email, current_user.id)
                current_user.image = picture_file

            new_email = form.email.data

            # Check if the new email already exists in the database
            user_with_new_email = User.query.filter_by(email=new_email).first()
            if user_with_new_email and user_with_new_email.id != current_user.id:
                message = "The email address is already in use. Please choose a different one."
                message_type = "danger"
            else:
                current_user.email = form.email.data
                current_user.firstname = form.firstname.data
                current_user.lastname = form.lastname.data
                current_user.date_of_birth = form.date_of_birth.data
                db.session.commit()
                message = 'Your changes have been saved.'
                message_type = 'success'
            
        except SQLAlchemyError:
            db.session.rollback()
            message = 'An error occurred while saving your changes. Please try again.'
            message_type = 'danger'

        return render_template('view_profile.html', title='View Profile', form=form, image_file=image, message=message, message_type=message_type)
    elif not form.validate_on_submit():
        if form.errors:
            message = next(iter(form.errors.values()))[0]
            message_type = 'danger'
        else:
            message = 'An error occurred while saving your changes. Please check if inputs make sense.'
            message_type = 'danger'
        return render_template('view_profile.html', title='View Profile', form=form, image_file=image, message=message, message_type=message_type)


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

@main.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        new_feedback = Feedback(
            companyId=current_user.companyId, 
            description=form.description.data
        )
        db.session.add(new_feedback)
        db.session.commit()
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('feedback'))
    return render_template('feedback.html', form=form)


# manager specific
@main.route('/team_test_history', methods=['GET'])
@login_required
def team_test_history():
    # Aggregate the results by testDate
    aggregated_results = (
        db.session.query(
            Results.testDate,
            func.avg(Results.scoreA).label('avg_scoreA'),
            func.avg(Results.scoreB).label('avg_scoreB'),
            func.avg(Results.scoreC).label('avg_scoreC')
        )
        .join(User, User.id == Results.user_id)
        .filter(User.manager_id == current_user.id)
        .group_by(Results.testDate)
        .order_by(Results.testDate.desc())
        .all()
    )

    return render_template(
        'team_test_history.html',
        title='Team Test History',
        aggregated_results=aggregated_results
    )

# @main.route('/select_manager', methods=['GET', 'POST'])
# @login_required
# def select_manager():
#     form = SelectManagerForm()
#     form.manager.choices = [(0, 'None')] + [(u.id, f'{u.firstname} {u.lastname}') for u in User.query.filter_by(companyId=current_user.companyId).all() if u.id != current_user.id]
#     if form.validate_on_submit():
#         current_user.manager_id = form.manager.data
#         db.session.commit()
#         flash('Your manager has been selected.')
#         return redirect(url_for('main.index'))  # redirect to the index page or any other page after manager selection
#     return render_template('select_manager.html', form=form)

# @main.before_request
# def before_request():
#     if current_user.is_authenticated and current_user.manager_id is None and request.endpoint not in ['main.select_manager', 'main.logout']:
#         return redirect(url_for('main.select_manager'))

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

#admin routes below
@main.route('/company/dashboard')
@login_required
def company_dashboard():
    # Make sure the current user is allowed to view the company dashboard (e.g., a company admin)
    if not current_user.role_id == 2:
        abort(403)

    # Fetch company-related data that you want to display on the dashboard
    # For demonstration, I'm fetching all users belonging to the company
    company_users = User.query.filter_by(companyId=current_user.companyId).all()
    # Assuming `company_users` is a list of user objects for a specific company
    user_ids = [user.id for user in company_users]
    results = Results.query.filter(Results.user_id.in_(user_ids)).all()

    company_id = current_user.companyId
    burnout_trends = get_burnout_trends()
    department_data = get_department_burnout_data(company_id)
    team_data = get_team_burnout_data(company_id)

    adminCount = User.query.filter_by(companyId=current_user.companyId, role_id=2).count()
    hrCount = User.query.filter_by(companyId=current_user.companyId, role_id=3).count()
    managerCount = User.query.filter_by(companyId=current_user.companyId, role_id=4).count()
    userCount = User.query.filter_by(companyId=current_user.companyId, role_id=5).count()

    def get_monthly_avg_for_roles(role_ids_mapping):
        """Returns monthly averages for different roles."""
        monthly_avg_by_role = {role: [0] * 12 for role in role_ids_mapping.keys()}

        for role, user_ids in role_ids_mapping.items():
            results = (
                db.session.query(
                    extract('month', Results.testDate).label('month'), 
                    func.round(100 * func.avg(Results.scoreA + Results.scoreB + Results.scoreC) / 132).label('avg_value')
                )
                .filter(Results.user_id.in_(user_ids))
                .group_by(extract('month', Results.testDate))
                .all()
            )

            for month, avg_value in results:
                monthly_avg_by_role[role][month-1] = avg_value

        return monthly_avg_by_role


    # Mapping roles to their respective user IDs
    role_ids_mapping = {
        'regular_users': [user.id for user in company_users if user.role_id == 5],
        'managers': [user.id for user in company_users if user.role_id == 4],
    }

    monthly_avgs = get_monthly_avg_for_roles(role_ids_mapping)


    # Pass all data to the template
    return render_template('admindashboard.html',
                            results=results, 
                           company_users=company_users, 
                           burnout_trends=burnout_trends,
                           department_data=department_data, 
                           team_data=team_data,
                           adminCount=adminCount,
                           hrCount=hrCount,
                           managerCount=managerCount,
                           userCount=userCount,
                           regular_users_avg=monthly_avgs['regular_users'],
                           manager_avg=monthly_avgs['managers'])



@main.route('/company/settings', methods=['GET', 'POST'])
@login_required
def company_settings():
    # Ensure the current user is authorized to edit the company settings
    if not current_user.role_id == 2:
        abort(403)

    message_type = ''
    message = ''

    form = CompanySettingsForm()

    if form.validate_on_submit():
        # Save company details
        current_user.company.name = form.companyName.data
        current_user.company.description = form.companyDescription.data
        current_user.company.size = form.companySize.data

        # Save the company logo if it was uploaded
        if form.companyLogo.data:
            logo_file = save_company_logo(form.companyLogo.data)
            current_user.company.image = logo_file
        
        db.session.commit()
        message_type = 'Success'
        message = 'Company settings updated successfully!'
        return redirect(url_for('main.company_settings'))

    elif form.errors:
        first_key = next(iter(form.errors))
        first_value = form.errors[first_key][0] if form.errors[first_key] else None
        message_type = 'danger'
        message = 'Error in field: ' + first_key + ' (' + first_value + ')'

    return render_template('adminsettingsconfig.html', form=form, message_type=message_type, message=message)


@main.route('/company/users', methods=['GET', 'POST'])
@login_required
def company_users():
    # Make sure the current user is allowed to manage company users
    if not (current_user.role_id == 3 or current_user.role_id == 2):
        abort(403)

    # Get page number from request arguments (or default to page 1 if not provided)
    page = request.args.get('page', 1, type=int)

    # Fetch paginated users from the company
    users_per_page = 25
    company_users = User.query.filter_by(companyId=current_user.companyId) \
        .paginate(page=page, per_page=users_per_page, error_out=False)

    # Build a mapping from managerId to email for quick lookup in the template
    manager_id_to_email = {user.id: user.email for user in User.query.all()}

    if current_user.role_id == 3:
        return render_template('hrusermanagement.html', users=company_users, manager_emails=manager_id_to_email)

    return render_template('adminusermanagement.html', users=company_users, manager_emails=manager_id_to_email)


@main.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not (current_user.role_id == 3 or current_user.role_id == 2):
        abort(403)

    user = User.query.get_or_404(user_id)

    # Retrieve manager's email if a manager is set for the user
    manager_email = user.manager.email if user.manager else ""

    form = UnifiedUserForm(original_email=user.email, obj=user)

    # For GET request
    if request.method == 'GET':
        form.role.data = user.role_id
        return render_template('edituser.html', title='Edit User', form=form, user=user)
    
    # For POST request
    if request.method == 'POST':
        
        # Form validation
        if not form.validate():
            print(form.errors)
            return render_template('edituser.html', title='Edit User', form=form, user=user)
        
        # Check if the new email already exists in the database and it's not the same as the original
        if form.email.data != user.email and User.query.filter_by(email=form.email.data).first():
            flash('This email is already in use. Please use a different one.', 'error')
            return render_template('edituser.html', title='Edit User', form=form, user=user)

        user.email = form.email.data
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.date_of_birth = form.date_of_birth.data
        user.role_id = int(form.role.data)
        user.title = form.title.data
        user.department = form.department.data

        # Updating the manager_id based on the manager's email
        manager = User.query.filter_by(email=form.manager_email.data).first()
        if manager:
            user.manager_id = manager.id
        else:
            user.manager_id = None

        db.session.commit()
        flash('User details have been updated.')
        return redirect(url_for('main.edit_user', user_id=user.id))



@main.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):

    if not (current_user.role_id == 2):
        abort(403)

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.email} has been deleted.')
    return redirect(url_for('main.company_users'))  # Or whichever route you want to redirect to after deletion


#hr routes below

@main.route('/hr/overview')
@login_required
def hr_overview():
    # Make sure the current user is allowed to view the company dashboard (e.g., a company admin)
    if not current_user.role_id == 3:
        abort(403)

    # Fetch company-related data that you want to display on the dashboard
    # For demonstration, I'm fetching all users belonging to the company
    company_users = User.query.filter_by(companyId=current_user.companyId).all()
    # Assuming `company_users` is a list of user objects for a specific company
    user_ids = [user.id for user in company_users]
    results = Results.query.filter(Results.user_id.in_(user_ids)).all()

    company_id = current_user.companyId

    burnout_trends = get_burnout_trends()
    department_data = get_department_burnout_data(company_id)
    team_data = get_team_burnout_data(company_id)

    adminCount = User.query.filter_by(companyId=current_user.companyId, role_id=2).count()
    hrCount = User.query.filter_by(companyId=current_user.companyId, role_id=3).count()
    managerCount = User.query.filter_by(companyId=current_user.companyId, role_id=4).count()
    userCount = User.query.filter_by(companyId=current_user.companyId, role_id=5).count()

    def get_monthly_avg_for_roles(role_ids_mapping):
        """Returns monthly averages for different roles."""
        monthly_avg_by_role = {role: [0] * 12 for role in role_ids_mapping.keys()}

        for role, user_ids in role_ids_mapping.items():
            results = (
                db.session.query(
                    extract('month', Results.testDate).label('month'), 
                    func.round(100 * func.avg(Results.scoreA + Results.scoreB + Results.scoreC) / 132).label('avg_value')

                )
                .filter(Results.user_id.in_(user_ids))
                .group_by(extract('month', Results.testDate))
                .all()
            )

            for month, avg_value in results:
                monthly_avg_by_role[role][month-1] = avg_value

        return monthly_avg_by_role

    # Mapping roles to their respective user IDs
    role_ids_mapping = {
        'regular_users': [user.id for user in company_users if user.role_id == 5],
        'managers': [user.id for user in company_users if user.role_id == 4],
    }

    monthly_avgs = get_monthly_avg_for_roles(role_ids_mapping)


    # Pass all data to the template
    return render_template('admindashboard.html',
                            results=results, 
                           company_users=company_users, 
                           burnout_trends=burnout_trends,
                           department_data=department_data, 
                           team_data=team_data,
                           adminCount=adminCount,
                           hrCount=hrCount,
                           managerCount=managerCount,
                           userCount=userCount,
                           regular_users_avg=monthly_avgs['regular_users'],
                           manager_avg=monthly_avgs['managers'])

@main.route('/hr/burnout-report')
@login_required
def hr_burnout_report():
    if not current_user.role_id == 3:
        abort(403)
    
    company_id = current_user.companyId

    def get_all_departments(company_id):
        # Query the User table for distinct department values for the given company
        distinct_departments = db.session.query(distinct(User.department)).filter_by(companyId=company_id).all()

        # Convert the result into a list of department strings
        departments = [department[0] for department in distinct_departments if department[0]]  # the if condition ensures we don't include None values

        return departments

    def get_all_managers(company_id):
        managers = User.query.filter_by(companyId=company_id, role_id=4).all()
        
        # Convert list of manager objects to a list of dictionaries
        manager_list = []

        # Add a default 'No Manager Assigned' option with an id of -1
        manager_list.append({
            'id': -1,
            'first_name': 'Users With No',
            'last_name': 'Manager Assigned'
        })

        for manager in managers:
            manager_dict = {
                'id': manager.id,
                'first_name': manager.firstname,
                'last_name': manager.lastname,
                # Add any other attributes of the manager you'd like to include
            }
            manager_list.append(manager_dict)

        return manager_list

    def replace_none_with_string(data):
        if isinstance(data, dict):
            keys_to_replace = [key for key in data if key is None or key == ""]
            for key in keys_to_replace:
                data[-1] = data.pop(key)

            for value in data.values():
                if isinstance(value, (dict, list)):
                    replace_none_with_string(value)
        return data

    # Fetching the various burnout data using helper functions
    department_data = get_department_burnout_data(company_id)
    team_data = get_team_burnout_data(company_id)
    departments = get_all_departments(company_id)
    managers = get_all_managers(company_id)
    team_data = replace_none_with_string(team_data)

    # You can also fetch any other necessary data related to burnout or general statistics that you want to show.

    print(department_data)
    print(team_data)
    print(departments)
    print(managers)
    # Passing the data to the template
    return render_template('hrreporting.html', 
                            department_data=department_data, 
                            team_data=team_data,
                            departments=departments,
                            managers=managers)


@main.route('/hr/edit-user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def hr_edit_user(user_id):
    if not current_user.role_id == 3:
        abort(403)

    user = User.query.get_or_404(user_id)
    form = HREditUserForm(obj=user)  # Use the new form here

    if form.validate_on_submit():
        user.email = form.email.data
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.date_of_birth = form.date_of_birth.data
        user.role = form.role.data

        db.session.commit()
        flash('User details updated!', 'success')
        return redirect(url_for('hr_user_management'))

    return render_template('edituser.html', form=form, user=user)

@main.route('/hr/feedback', methods=['GET', 'POST'])
@login_required
def hr_feedback():
    if not current_user.role_id == 3:
        abort(403)
    
    feedbacks = Feedback.query.filter_by(company_id=current_user.companyId).order_by(Feedback.date_submitted.desc()).all()

    return render_template('hrfeedback.html', feedbacks=feedbacks)

@main.route('/hr/feedback/change_status/<int:feedback_id>', methods=['POST'])
@login_required
def change_feedback_status(feedback_id):
    if not current_user.role_id == 3:
        return jsonify(success=False, message='Unauthorized access'), 403

    feedback = Feedback.query.get_or_404(feedback_id)

    feedback.status = "Reviewed"
    db.session.commit()

    return jsonify(success=True, message='Feedback status updated!')

@main.route('/testhtml', methods=['GET', 'POST'])
def testhtml():
    return render_template('intro.html')


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