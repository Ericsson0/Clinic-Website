from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader 
def load_user(user_id): 
    return User.query.get(int(user_id))


class Patient(db.Model, UserMixin): 
    __bind_key__ = 'patient'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(10), nullable=False)
    number = db.Column(db.String(11), unique=False, nullable=False) 
    gender = db.Column(db.String(2), nullable=False) 
    birth = db.Column(db.String(10), nullable=False) 
    IDcard = db.Column(db.String(12), nullable=False) # 身份证 
    create = db.Column(db.DateTime, nullable=False, default=datetime.now)   

class Detail(db.Model, UserMixin): 
    __bind_key__ = 'detail'
    id = db.Column(db.Integer, primary_key=True) 
    Symptom = db.Column(db.String(100), nullable=False)
    Initial_diagnosis = db.Column(db.String(50), nullable=False) 
    Preliminary_treatment_plan = db.Column(db.String(100), nullable=False) 
    Check_result = db.Column(db.String(50), nullable=False) 
    Patient_reason = db.Column(db.String(100), unique=False, nullable=False) 
    Formula = db.Column(db.String(100), unique=False, nullable=False)
    Date_of_diagnosis = db.Column(db.DateTime, nullable=False, default=datetime.now)   

class Medicine(db.Model): 
    __bind_key__ = 'medicine'
    id = db.Column(db.Integer, primary_key=True) 
    Vendor = db.Column(db.String(50), nullable=False)
    Quantity = db.Column(db.String(5), nullable=False) 
    Medicine_name = db.Column(db.String(30), nullable=False) 
    Deadline = db.Column(db.String(20), nullable=False) 
    Price = db.Column(db.String(10), nullable=False) 
    How_to_use = db.Column(db.String(100), nullable=False) 
    time_get = db.Column(db.DateTime, nullable=False, default=datetime.now) 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    department = db.Column(db.String(30), unique=False, nullable=False)
    create = db.Column(db.DateTime, nullable=False, default=datetime.now) 
    password = db.Column(db.String(60), nullable=False) 
    worklogs = db.relationship('Worklog', backref='author', lazy=True) 
    announcements = db.relationship('Announcement', backref='author', lazy=True)  
    announcements = db.relationship('Announcement', backref='author', lazy=True)  

class Admin(db.Model, UserMixin):
    __bind_key__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=True, default='admin')
    create = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.now) 
    password = db.Column(db.String(60), nullable=False, default='admin') 

class Worklog(db.Model):  
    __bind_key__ = 'work_log'
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(20), unique=False, nullable=False)
    body = db.Column(db.String(300), unique=False, nullable=False)
    tag = db.Column(db.String(50), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
         
class Announcement(db.Model):
    __bind_key__ = 'announcement'
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(20), unique=False, nullable=False)
    body = db.Column(db.String(200), unique=False, nullable=False) 
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  

     