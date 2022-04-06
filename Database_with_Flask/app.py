import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# dir for database,  __file__: C:\Users\ASUS\Desktop\Web-Flask\Database with Flask
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
# database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app,db)

# Create a Model
class Puppy (db.Model):
    # manual table name 
    __tablename__ = 'puppies'

    # Create columns for database
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age,breed):
        self.name = name 
        self.age = age
        self.breed = breed

    # __repr__ gives the string representation of the object.
    def __repr__(self):
        return f" Puppy {self.name} is {self.age} year/s old"


