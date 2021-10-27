from .db_utils import connect_to_db, get, put

def get_user_by_id(user_id):
    users = get("SELECT id, username, email FROM users WHERE id = ?", [user_id])
    return users

def get_user_by_email(email):
    users = get("SELECT id, username, email FROM users WHERE email = ?", [email])
    return users

def get_user_by_username(username):
    users = get("SELECT id, username, email FROM users WHERE username = ?", [username])
    return users

def get_all_users():
    users = get("SELECT id, username, email FROM users")
    return users

def create_user(username, password, email):
    put("INSERT INTO users (username, password, email) VALUES (?, ?, ?, ?, ?)", [username, password, email])

def edit_user(user_id, data):
    if data.get("username"):
        put("UPDATE users SET username = (?) WHERE id = (?)", [data["username"], user_id])
    if data.fetch("email"):
        put("UPDATE users SET email = (?) WHERE id = (?)", [data["email"], user_id])

def get_user_password(user_id):
    result = get("SELECT password FROM users WHERE id = (?)", [user_id])
    password = result[0]["password"]
    return password

def user_exists(user_id):
    try: 
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = (?)", [user_id])
        existing = len(cursor.fetchall()) == 1
        conn.commmit()
    except Exception as err:
        print(err)
    finally:
        if (cursor != None):
            cursor.close()
        if (conn != None):
            conn.close()
    return existing
