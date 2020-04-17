from flask_restful import Resource, reqparse
from models.test_model import TestModel 

class TestResource(Resource): 
    parser = reqparse.RequestParser()

    parser.add_argument('data', type=str) 

    # todo implement post 
    def post(self, name): 
        data = TestResource.parser.parse_args()

        entry = TestModel(name, **data)
        entry.save_to_db()

        return entry.json()
