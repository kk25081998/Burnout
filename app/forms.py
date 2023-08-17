# app/forms.py
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, URL, NumberRange, InputRequired
from app.models import User
from wtforms import TextAreaField, SelectField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, FileField, RadioField
from datetime import datetime
# from email_validator import validate_email, EmailNotValidError

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Please enter a valid email address')])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    companyId = IntegerField('Company ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already in use.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class PasswordChangeForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[InputRequired()])
    new_password = PasswordField('New Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm New Password', validators=[InputRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')

class EditProfileForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d')
    image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

class TakeTest(FlaskForm):
    # Define ratings as choices
    ratings = [(str(i), str(i)) for i in range(7)]

    # Section 1
    q1 = RadioField('I feel emotionally drained by my work.', choices=ratings, validators=[DataRequired()])
    q2 = RadioField('Working with people all day long requires a great deal of effort.', choices=ratings, validators=[DataRequired()])
    q3 = RadioField('I feel like my work is breaking me down.', choices=ratings, validators=[DataRequired()])
    q4 = RadioField('I feel frustrated by my work.', choices=ratings, validators=[DataRequired()])
    q5 = RadioField('I feel I work too hard at my job.', choices=ratings, validators=[DataRequired()])
    q6 = RadioField('It stresses me too much to work in direct contact with people.', choices=ratings, validators=[DataRequired()])
    q7 = RadioField('I feel like I’m at the end of my rope.', choices=ratings, validators=[DataRequired()])

    # Section 2
    q8 = RadioField('I feel I look after certain patients/clients impersonally, as if they are objects.', choices=ratings, validators=[DataRequired()])
    q9 = RadioField('I feel tired when I get up in the morning and have to face another day at work.', choices=ratings, validators=[DataRequired()])
    q10 = RadioField('I have the impression that my patients/clients make me responsible for some of their problems.', choices=ratings, validators=[DataRequired()])
    q11 = RadioField('I am at the end of my patience at the end of my work day.', choices=ratings, validators=[DataRequired()])
    q12 = RadioField('I really don’t care about what happens to some of my patients/clients.', choices=ratings, validators=[DataRequired()])
    q13 = RadioField('I have become more insensitive to people since I’ve been working.', choices=ratings, validators=[DataRequired()])
    q14 = RadioField('I’m afraid that this job is making me uncaring.', choices=ratings, validators=[DataRequired()])

    # Section 3
    q15 = RadioField('I accomplish many worthwhile things in this job.', choices=ratings, validators=[DataRequired()])
    q16 = RadioField('I feel full of energy.', choices=ratings, validators=[DataRequired()])
    q17 = RadioField('I am easily able to understand what my patients/clients feel.', choices=ratings, validators=[DataRequired()])
    q18 = RadioField('I look after my patients’/clients’ problems very effectively.', choices=ratings, validators=[DataRequired()])
    q19 = RadioField('In my work, I handle emotional problems very calmly.', choices=ratings, validators=[DataRequired()])
    q20 = RadioField('Through my work, I feel that I have a positive influence on people.', choices=ratings, validators=[DataRequired()])
    q21 = RadioField('I am easily able to create a relaxed atmosphere with my patients/clients.', choices=ratings, validators=[DataRequired()])
    q22 = RadioField('I feel refreshed when I have been close to my patients/clients at work.', choices=ratings, validators=[DataRequired()])

    # Global submit button
    submit = SubmitField('Submit')

class SelectManagerForm(FlaskForm):
    manager = SelectField('Manager', coerce=int, choices=[(0, 'None')]) # default choice for None
    submit = SubmitField('Submit')