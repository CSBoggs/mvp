from flask import Blueprint, jsonify, make_response, Response, request
from ..security.security_utils import generate_token
from db import db_sessions, db_users
import bcrypt

login = Blueprint("/api/login", __name__)

@login.route("/api/login", methods=["POST"])
def user_login():
    try:
        data = request.get_json()
        email = data["email"]
        provided_pword = data["password"].encode()
        user = db_users.get_user_by_email(email)
        stored_pword = db_users.get_user_password(user[0]["userId"])

        if bcrypt.checkpw(provided_pword.encode(), stored_pword):
            db_sessions.login_user(user[0]["userId"])
            token = generate_token(user[0]["userId"])
            user[0].update({'loginToken': token})
            print(token)
            return make_response(jsonify(user), 200)
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


    
