# app/forms.py
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import (
    DataRequired,
    ValidationError,
    Email,
    EqualTo,
    URL,
    NumberRange,
    InputRequired,
    Optional,
    Length,
    Regexp,
)
from app.models import User, Company, Role
from wtforms import TextAreaField, SelectField
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    IntegerField,
    DateField,
    FileField,
    RadioField,
)
from datetime import datetime

INDUSTRY_CHOICES = [
    ("Agriculture", "Agriculture"),
    ("Automotive", "Automotive"),
    ("Banking", "Banking"),
    ("Construction", "Construction"),
    ("Education", "Education"),
    ("Energy", "Energy"),
    ("Entertainment", "Entertainment"),
    ("Fashion", "Fashion"),
    ("Finance", "Finance"),
    ("Food & Beverage", "Food & Beverage"),
    ("Healthcare", "Healthcare"),
    ("Hospitality", "Hospitality"),
    ("Information Technology", "Information Technology"),
    ("Insurance", "Insurance"),
    ("Legal", "Legal"),
    ("Manufacturing", "Manufacturing"),
    ("Media", "Media"),
    ("Mining", "Mining"),
    ("Pharmaceuticals", "Pharmaceuticals"),
    ("Real Estate", "Real Estate"),
    ("Retail", "Retail"),
    ("Telecommunication", "Telecommunication"),
    ("Transportation", "Transportation"),
    ("Travel", "Travel"),
    ("Utilities", "Utilities"),
    ("Others", "Others"),
]


class CompanyRegistrationForm(FlaskForm):
    # User fields
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Please enter a valid email address"),
        ],
    )
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    date_of_birth = DateField(
        "Date of Birth", format="%Y-%m-%d", validators=[DataRequired()]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )

    # Company fields
    company_name = StringField("Company Name", validators=[DataRequired()])
    company_description = StringField(
        "Company Description", validators=[DataRequired()]
    )
    company_size = IntegerField("Company Size")
    industry = SelectField(
        "Industry", validators=[DataRequired()], choices=INDUSTRY_CHOICES
    )

    submit = SubmitField("Register for Company")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already in use.")


class IndividualRegistrationForm(FlaskForm):
    # User fields
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Please enter a valid email address"),
        ],
    )
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    date_of_birth = DateField(
        "Date of Birth", format="%Y-%m-%d", validators=[DataRequired()]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    title = StringField(
        "Title (e.g., Freelancer, Consultant)", validators=[DataRequired()]
    )

    # Company fields for individual subscriber (as a business entity)
    company_name = StringField(
        "Company Name or Freelance Name", validators=[DataRequired()]
    )
    company_description = StringField(
        "Description for what you do", validators=[DataRequired()]
    )
    industry = SelectField(
        "Industry", validators=[DataRequired()], choices=INDUSTRY_CHOICES
    )

    submit = SubmitField("Register as Individual")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already in use.")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Please enter a valid email address"),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class PasswordChangeForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[InputRequired()])
    new_password = PasswordField("New Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm New Password", validators=[InputRequired(), EqualTo("new_password")]
    )
    submit = SubmitField("Change Password")


class EditProfileForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Invalid email was entered")]
    )
    firstname = StringField("First Name")
    lastname = StringField("Last Name")
    date_of_birth = DateField("Date of Birth", format="%Y-%m-%d")
    image = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")


class TakeTest(FlaskForm):
    # Define ratings as choices
    ratings = [(str(i), str(i)) for i in range(7)]

    # Section 1
    q1 = RadioField(
        "I feel emotionally drained by my work.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q2 = RadioField(
        "Working with people all day long requires a great deal of effort.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q3 = RadioField(
        "I feel like my work is breaking me down.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q4 = RadioField(
        "I feel frustrated by my work.", choices=ratings, validators=[DataRequired()]
    )
    q5 = RadioField(
        "I feel I work too hard at my job.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q6 = RadioField(
        "It stresses me too much to work in direct contact with people.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q7 = RadioField(
        "I feel like I’m at the end of my rope.",
        choices=ratings,
        validators=[DataRequired()],
    )

    # Section 2
    q8 = RadioField(
        "I feel I look after certain patients/clients impersonally, as if they are objects.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q9 = RadioField(
        "I feel tired when I get up in the morning and have to face another day at work.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q10 = RadioField(
        "I have the impression that my patients/clients make me responsible for some of their problems.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q11 = RadioField(
        "I am at the end of my patience at the end of my work day.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q12 = RadioField(
        "I really don’t care about what happens to some of my patients/clients.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q13 = RadioField(
        "I have become more insensitive to people since I’ve been working.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q14 = RadioField(
        "I’m afraid that this job is making me uncaring.",
        choices=ratings,
        validators=[DataRequired()],
    )

    # Section 3
    q15 = RadioField(
        "I accomplish many worthwhile things in this job.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q16 = RadioField(
        "I feel full of energy.", choices=ratings, validators=[DataRequired()]
    )
    q17 = RadioField(
        "I am easily able to understand what my patients/clients feel.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q18 = RadioField(
        "I look after my patients’/clients’ problems very effectively.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q19 = RadioField(
        "In my work, I handle emotional problems very calmly.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q20 = RadioField(
        "Through my work, I feel that I have a positive influence on people.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q21 = RadioField(
        "I am easily able to create a relaxed atmosphere with my patients/clients.",
        choices=ratings,
        validators=[DataRequired()],
    )
    q22 = RadioField(
        "I feel refreshed when I have been close to my patients/clients at work.",
        choices=ratings,
        validators=[DataRequired()],
    )

    # Global submit button
    submit = SubmitField("Submit")


class SelectManagerForm(FlaskForm):
    manager = SelectField(
        "Manager", coerce=int, choices=[(0, "None")]
    )  # default choice for None
    submit = SubmitField("Submit")


def validate_length(form, field):
    length = len(str(field.data))
    if length < 10 or length > 12:
        raise ValidationError("Field must be between 10 and 12 digits long.")


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=150)])
    telephone = StringField("Telephone", validators=[Optional(), validate_length])
    reason = SelectField(
        "Reason for Contact",
        choices=[
            ("", "Select Reason"),
            ("get_quote", "Get a Quote"),
            ("general_inquiry", "General Inquiry"),
            ("bug_report", "Bug Report")
            # Add more options as needed
        ],
        validators=[DataRequired()],
        default="",
        render_kw={"placeholder": "Please select a reason..."},
    )
    subject = StringField(
        "Subject",
        validators=[Optional(), Length(max=200)],
        default="",
        render_kw={"placeholder": "Optional Subject..."},
    )
    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(max=1000)],
        render_kw={"placeholder": "Enter your message here..."},
    )


def valid_manager_email(form, field):
    if field.data:
        # Check if email is present in the user database (i.e., a valid manager)
        user = User.query.filter_by(email=field.data).first()
        if user is None:
            raise ValidationError("Please enter a valid manager email.")


class UnifiedUserForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Invalid email was entered")]
    )
    firstname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    lastname = StringField(
        "Last Name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    date_of_birth = StringField("Date of Birth", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=100)])
    department = SelectField(
        "Department", choices=[], validators=[DataRequired()]
    )  # Empty choices for now
    manager_email = StringField(
        "Manager Email", validators=[Optional(), Length(max=120), valid_manager_email]
    )

    role = SelectField(
        "Role",
        coerce=int,
        choices=[(5, "User"), (2, "Admin"), (3, "HR"), (4, "Manager")],
        validators=[DataRequired()],
    )

    submit = SubmitField("Update User Details")
    delete = SubmitField("Delete User")

    def __init__(self, original_email=None, *args, **kwargs):
        super(UnifiedUserForm, self).__init__(*args, **kwargs)
        self.original_email = original_email
        if "all_departments" in kwargs:
            self.department.choices = [(dep, dep) for dep in kwargs["all_departments"]]

    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=self.email.data).first()
            if user is not None:
                raise ValidationError("Please use a different email address.")


class FeedbackForm(FlaskForm):
    feedback = TextAreaField(
        "Feedback", validators=[DataRequired(), Length(min=5, max=1000)]
    )
    submit = SubmitField("Submit")


class CompanySettingsForm(FlaskForm):
    companyName = StringField("Company Name", [DataRequired(), Length(min=1, max=200)])
    companyDescription = StringField(
        "Company Description", [DataRequired(), Length(min=1, max=500)]
    )
    companySize = IntegerField(
        "Company Size", [DataRequired(), NumberRange(min=1, max=1000000)]
    )
    # companyFrequency = SelectField('Feedback Frequency', [DataRequired()],
    #                                choices=[('1_week', '1 Week'),
    #                                         ('2_weeks', '2 Weeks'),
    #                                         ('1_month', '1 Month'),
    #                                         ('2_months', '2 Months')])
    companyLogo = FileField(
        "Upload Company Logo", validators=[Optional(), FileAllowed(["jpg", "png"])]
    )
    submit_settings = SubmitField("Update Settings")


class CreateNewUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    role = SelectField(
        "Role", choices=[], validators=[DataRequired()]
    )  # Choices can be populated dynamically from the Role table
    title = StringField("Title", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Create")
