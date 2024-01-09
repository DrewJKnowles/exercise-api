from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init App 
app = Flask(__name__)
# Sets the base path
basedir = os.path.abspath(os.path.dirname(__file__))
# Set the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Excercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)   
    description = db.Column(db.String(200))
    howToDescription = db.Column(db.String(200))
    
    def __init__(self, name, description, howToDescription):
        self.name = name
        self.description = description
        self.gifLocation = howToDescription

class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'howToDescription')
        
# Init Schema 
exercise_schema = ExerciseSchema(strict=True)    
exercises_schema = ExerciseSchema(many=True, strict=True)


# class MuscleGroups(db.Model):
#     muscle_group_id = db.Column(db.integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)      
    
#     def __init__(self, name):
#         self.name = name       
         
# class ExerciseGifs(db.Model):
#     gif_id = db.Column(db.integer, primary_key=True)
#     exercise_id = db.Column(db.integer)    
#     description = db.Column(db.String(200))
#     url = db.Column(db.String(200))  
    
#     def __init__(self, exercise_id, description, url):
#         self.exercise_id = exercise_id  
#         self.description = description
#         self.url = url        
      
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'helloWorld'})

# Run Server
if __name__ == '__main__':
    app.run(debug=True)