import sqlite3
from debug import DEBUG

user_db_name = "users.db"
table_name = "users"

def connect():
    DEBUG("connect()")
    return sqlite3.connect(user_db_name)

def disconnect(conn):
    DEBUG("disconnect()")
    conn.close()

def create_db(conn):
    DEBUG("create_db()")
    conn.execute("create table if not exists " + table_name + " (id integer)")
    conn.commit()
