from flask import Blueprint

api_1_0 = Blueprint('api_1_0', __name__, url_prefix='/api')

from . import users
