from flask import make_response, jsonify, request
from datetime import date, datetime, timedelta
import jwt

def generate_token(user_id):
    expiry = datetime.utcnow() + timedelta(minutes=+60)
    token = jwt.encode(
        {
            "expiry": expiry,
            "user_id": user_id
        }
    )
    return token
