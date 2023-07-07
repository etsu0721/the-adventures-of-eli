from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # image files hashed to be 20 characters long
    password = db.Column(db.String(60), nullable=False) # passwords hashed to be 60 characters long

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}', '{self.image_file}')"
    

# Association table
activity_gear = db.Table(
    'user_activity_gear',
    # db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('activity_id', db.Integer, db.ForeignKey('activity.id')),
    db.Column('gear_id', db.Integer, db.ForeignKey('gear.id'))
)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    equipment = db.relationship('Gear', secondary=activity_gear, backref='activities')

    def __repr__(self):
        return f"Activity('{self.id}', '{self.name}')"


class Gear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    retired = db.Column(db.Boolean, nullable=False, default=False)
    retired_date = db.Column(db.DateTime)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"Gear('{self.id}', '{self.brand}', '{self.model}', '{self.nickname}')"
