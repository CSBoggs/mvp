from .db_utils import get, put

def login_user(user_id):
    put("REPLACE INTO user_sessions (users_id) VALUES (?)", [user_id])

def logout_user(user_id):
    put("DELETE FROM user_sessions WHERE users_id = (?)", [user_id])

def is_logged_in(user_id):
    if get("SELECT * FROM user_sessions WHERE users_id = (?)", [user_id]):
        return True
    else:
        return False

def fetch_user_id_login_token(login_token):
    result = get("SELECT users_id FROM user_sessions WHERE login_token= (?)", [login_token])
    user_id = result[0]["users_id"]
    return user_id

def update_login_token(login_token, user_id):
    put("UPDATE user_sessions SET login_token = (?) WHERE users_id = (?)", [login_token, user_id])