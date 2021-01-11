from flask import request
from . import routes
from app.utils import add_user

@routes.route('/users', methods=['POST'])
def add_user_route():
    return add_user(request)