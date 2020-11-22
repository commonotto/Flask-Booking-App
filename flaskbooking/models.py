from datetime import datetime
from flaskbooking import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    payment = db.Column(db.Boolean, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Event('{self.title}', '{self.start_time}', ' {self.end_time}', ' {self.payment}')"

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(100), nullable = False)
    l_name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(10), nullable = False)
    f_name2 = db.Column(db.String(100), nullable = False)
    l_name2 = db.Column(db.String(100), nullable = False)
    phone2 = db.Column(db.String(10), nullable = False)
    street_address = db.Column(db.String(100), nullable = False)
    city = db.Column(db.String(100), nullable = False)
    state = db.Column(db.String(100), nullable = False)
    zip_code = db.Column(db.String(100), nullable = False)