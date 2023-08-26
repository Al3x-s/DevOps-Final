import sqlite3
def check_if_user_exists(user_email):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (user_email,))
    result = cursor.fetchone()
    conn.close()
    #print(result)
    return result is not None


def check_user_updated(email, password):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE email = ? AND password = ?"

    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def user_pass_incorrect():
    x = "User password is incorrect"
    return x

def add_user(email,password):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    query = "INSERT INTO users (email, password) VALUES (?,?)"
    cursor.execute(query,(email,password))
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
    conn.close()
