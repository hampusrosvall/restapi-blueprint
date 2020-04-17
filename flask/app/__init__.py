from flask import Flask 
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy() 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

# these imports need to be below the initialization of the app, api and database due to circular imports 
from resources.health import Health
from resources.test_resource import TestResource

api.add_resource(Health, '/')
api.add_resource(TestResource, '/test/<string:name>')

