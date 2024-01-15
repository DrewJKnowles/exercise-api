''' Import Packages '''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema
from dotenv import load_dotenv

''' Load and Kick Python '''
load_dotenv()

from routes import *
from database import db


# Init App
app = Flask(__name__)
app.register_blueprint(routes)


ma = Marshmallow(app)    

# Build DB Tables and Information 
with app.app_context():
    db.create_all()
# Build DB Tables and Information 
with app.app_context():
    db.create_all()
# Run Server
if __name__ == '__main__':
    app.run(debug=True)
