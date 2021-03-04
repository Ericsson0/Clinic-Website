from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import InputRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, NumberRange
from flaskblog.models import User

class DetailForm(FlaskForm):
    Symptom = StringField('Symptom', validators=[DataRequired(), Length(min=2, max=100)]) 
    Initial_diagnosis = StringField('Initial_diagnosis', validators=[DataRequired(), Length(min=2, max=50)]) 
    Preliminary_treatment_plan = StringField('Preliminary_treatment_plan', validators=[DataRequired(), Length(min=2, max=100)]) 
    Check_result = StringField('Check_result', validators=[DataRequired(), Length(min=2, max=50)])
    Patient_reason = StringField('Patient_reason', validators=[DataRequired(), Length(min=2, max=100)]) 
    Formula = StringField('Formula', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('添加') 

class MedicineForm(FlaskForm):
    Vendor = StringField('Vendor', validators=[DataRequired(), Length(min=2, max=50)]) 
    Quantity = StringField('Quantity', validators=[DataRequired(), Length(min=2, max=5)]) 
    Medicine_name = StringField('Medicine', validators=[DataRequired(), Length(min=2, max=30)]) 
    Deadline = StringField('Deadline', validators=[DataRequired(), Length(min=2, max=20)]) 
    Price = StringField('Price', validators=[DataRequired(), Length(min=2, max=10)])
    How_to_use = StringField('How_to_use', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('添加') 

class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    department = StringField('department',
                        validators=[DataRequired(), Length(min=2, max=30)])  
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('That name is taken. Please choose a different one.')

    def validate_email(self, phone):
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    name = StringField('name',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('登录')

class PatientForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)]) 
    number = StringField('number', validators=[DataRequired(), Length(min=11, max=11)]) 
    gender = StringField('gender', validators=[DataRequired(), Length(min=1, max=2)]) 
    birth = StringField('birth', validators=[DataRequired(), Length(min=10, max=10)])
    IDcard = StringField('card', validators=[DataRequired(), Length(min=18, max=20)])  
    submit = SubmitField('添加')  

class AddWorkLogForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=2, max=20)]) 
    body = StringField('body', validators=[DataRequired(), Length(min=2, max=300)]) 
    tag = StringField('tag', validators=[DataRequired(), Length(min=2, max=50)]) 
    submit = SubmitField('添加')

class UpdateDoctorForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    department = StringField('department',
                        validators=[DataRequired(), Length(min=2, max=30)])  
    submit = SubmitField('确认')

    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first() 
        if user:
            raise ValidationError('That name is taken. Please choose a different one.')
     
class UpdateDoctorPasswordForm(FlaskForm): 
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('确认')

class AdminLoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)]) 
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('登录')

class AdminRegistrationForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

class AddannouncementForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=2, max=20)])
    body = StringField('body', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('发布')