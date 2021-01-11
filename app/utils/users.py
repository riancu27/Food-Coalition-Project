from flask import jsonify
from app.store import add_user_mongo

def add_user(req): 
    user = add_user_mongo(req.json)
    return jsonify(user), 200