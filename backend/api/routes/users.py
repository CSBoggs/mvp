from flask import Flask, request, make_response, jsonify, Response, Blueprint
from ..db import db_users
import bcrypt 

users = Blueprint('/api/users', __name__)

@users.route('/api/users', methods=["GET"])
def get_users():
    userId = None

    try: 
        userId = request.args['userId']
    except Exception as err:
        print(err)
    
    if userId:
        user = db_users.get_user_by_id(userId)
        if user:
            return make_response(jsonify(user), 200)
        else:
            return make_response(jsonify({"message": "User was not found with that user ID"}), 400)
    else:
        all = db_users.get_all_users()
        if not all:
            return make_response(jsonify({"message": "No users found"}), 400)
        else:
            return make_response(jsonify(all), 200)

@users.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        salt = bcrypt.gensalt()
        username = data["username"]
        password = bcrypt.hashpw(data["password"].encode(), salt)
        email = data["email"]

        try:
            user_exists = db_users.get_user_by_email(email) or db_users.get_user_by_username(username)
            if user_exists:
                return make_response(jsonify({"message": "Incorrect data provided"}), 400)
        except:
            pass
    except:
        return make_response(jsonify({"message": "Incorrect data provided"}), 400)
    else:
        db_users.create_user(username, password, email)
        created_user = db_users.get_user_by_username(username)
        return make_response(jsonify(created_user), 201)

@users.route("/api/users", methods=["PATCH"])
def edit_user(user_id):
    data = request.get_json()
    params = {"username", "email"}
    edit_data = [0] in params, data.items()

    if edit_data:
        db_users.edit_user(user_id, data)
    else:
        return make_response(jsonify({"message": "Incorrect data provided"}), 400)
    return make_response(jsonify({"message": "Updated user information"}), 201)