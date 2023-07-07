from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

# Flask app configured with SQL and No-SQL database 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c87cf4f86058cdfa763cf4d340a0908f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/adventures'

db = SQLAlchemy(app)
app.app_context().push()

#TODO: Adventures should be a NoSQL database collection, not a SQL database table, and needs to be implemented as such
# class Adventure(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=dt.utcnow)

# client = MongoClient('localhost', 27017)
# mongo_db = client.flask_db
# adventures_collection = mongo_db.adventures

from app import routes