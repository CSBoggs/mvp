from .db_utils import get, put

def add_char_to_roster(role_id, user_id, character_name):
    put("INSERT INTO roster (role, users_id, name) VALUES (?, ?, ?)", [role_id, user_id, character_name])
