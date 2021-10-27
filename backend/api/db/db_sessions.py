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