from flask_restful import Api, Resource
from flask import url_for
from . import api_1_0

api = Api(api_1_0)

class UserAPI(Resource):
    def get(self):
        return "sdfsdf{}".format('aaaaaaa')
        # pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/users', endpoint = 'users')