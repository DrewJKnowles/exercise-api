''' Import Packages '''
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema
from dotenv import load_dotenv

''' Load and Kick Python '''
load_dotenv()

from routes import *

# Init App
app = Flask(__name__)
# Sets the base path
basedir = os.path.abspath(os.path.dirname(os.environ.get("DATABASE_LOCATION")))
# Set the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(routes)

db = SQLAlchemy(app)
ma = Marshmallow(app)    



'''
Exercise DB Class
'''
class Excercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    howToDescription = db.Column(db.String(200))

    def __init__(self, name, description, howToDescription):
        self.name = name
        self.description = description
        self.gifLocation = howToDescription

'''
Exercise DB Schema
'''
class ExerciseSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'howToDescription')


# Init Schema
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

# Build DB Tables and Information 
with app.app_context():
    db.create_all()
# Run Server
if __name__ == '__main__':
    app.run(debug=True)
