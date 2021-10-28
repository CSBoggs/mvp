import mariadb
from mariadb import connect
from flask import jsonify
import dbcreds

conn = None
cursor = None

def connect_to_db():
    return connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )

def get(command, arguments =[]):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(command, arguments)
        row_headers = [x[0] for x in cursor.description]
        row_values = cursor.fetchall()
        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers, result)))
        result = json_data
    except mariadb.OperationalError:
        print("Something is wrong with the connection")
    except Exception as err:
        print(err)
    else:
        if (cursor != None):
            cursor.close()
        if (conn != None):
            conn.close()
    return result

def put(command, arguments =[]):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(command, arguments)
        conn.commit()
    except mariadb.OperationalError:
        print("Something is wrong with the connection")
    except Exception as err:
        print(err)
    else:
        if (cursor != None):
            cursor.close()
        if (conn != None):
            conn.close()