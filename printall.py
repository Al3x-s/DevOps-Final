import sqlite3
def printall():
    print("========================================")
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
    conn.close
printall()
