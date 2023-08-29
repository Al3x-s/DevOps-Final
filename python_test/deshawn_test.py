#!/usr/bin/python3
from main import app
import os
import sqlite3

database_path = "DevOps-Final/user.db"
conn = sqlite3.connect(database_path)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   email TEXT NOT NULL, 
                   password TEXT NOT NULL,
                   image TEXT NOT NULL DEFAULT "image.png",
                   name TEXT NOT NULL DEFAULT "",
                   quote TEXT NOT NULL DEFAULT "",
                   submission INTEGER NOT NULL DEFAULT "0"
               )''')
conn.commit()
def db_connection():
    conn = sqlite3.connect(database_path)
    yield conn
    conn.close()

# Test: Check if there are names in the database
def test_name_in_database(db_connection):
    conn = db_connection
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    assert result[0] > 0

# Run the tests
if __name__ == "__main__":
    pytest.main()
