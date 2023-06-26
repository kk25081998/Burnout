# app/forms.py
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, URL, NumberRange
from app.models import User
from wtforms import TextAreaField, SelectField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, FileField
from datetime import datetime
# from email_validator import validate_email, EmailNotValidError

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email address')])
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
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class EditProfileForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    bio = TextAreaField('Bio')
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d')
    image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


