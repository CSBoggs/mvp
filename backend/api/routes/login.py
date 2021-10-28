from flask import Blueprint, jsonify, make_response, Response, request
from ..db import db_sessions, db_users
import bcrypt
from uuid import uuid4

login = Blueprint("/api/login", __name__)

@login.route("/api/login", methods=["POST"])
def user_login():
    try:
        data = request.get_json()
        username = data["username"]
        userId = db_users.get_user_by_username(username)
        provided_pword = data["password"].encode()
        hashed = bcrypt.hashpw(db_users.get_user_password(userId[0]["id"]).encode(), bcrypt.gensalt())
        
        if bcrypt.checkpw(provided_pword, hashed):
            db_sessions.login_user(userId[0]["id"])
            token = uuid4()
            db_sessions.update_login_token(str(token), userId[0]["id"])
            print(token)
            return make_response(jsonify(username), 200)
        else:
            return make_response(jsonify({"message": "Username and/or password do not match"}), 409)
    except Exception as err:
        print(err)
        return make_response(jsonify({"message": "Incorrect data provided"}), 400)

@login.route("/api/login", methods=["DELETE"])
def user_logout():
    user = None
    try:
        data = request.get_json()
        provided_token = data["login_token"]
        user = data["userId"]
        stored_token = db_sessions.fetch_login_token(user[0]["users_id"])
        if str(provided_token) == str(stored_token):
            db_sessions.logout_user(user[0]["id"])
            return make_response(jsonify(user),200)
    except Exception as err:
        print (err)
        return make_response(jsonify({"message": "Invalid token"}), 400)


    
