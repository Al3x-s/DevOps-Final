#!/usr/bin/env python
from flask import Flask, render_template, session, request, url_for, redirect
import sqlite3
from functions import *

app = Flask(__name__)
app.secret_key = "a6sidg7fo8hyug2irhyug7hd8owiundilfaud"

#AS
conn = sqlite3.connect('user.db')
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

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        x = ''
        username = request.form.get("email")
        password = request.form.get("password")
        #if user info isnt in databse add it otherwise log in
        if check_if_user_exists(username): # chheck if user email is in datdabase
            print(check_if_user_exists(username))
            print("++++++++++++++++++++++++++++++++++")
            if check_user_updated(username, password): # if both user and pass exist
                session["logged_in"] = True
                session["email"] = username
                print(check_user_updated(username, password))
                print("second if")
                return redirect(url_for('home'))
            else:
                x = user_pass_incorrect()
                print("first else")
                return render_template("login.html", incorrect = x)
        else:
            add_user(username, password)
            print("add user")
            return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if 'logged_in' in session and session['logged_in']:
        if request.method == "POST":
            name = request.form.get("name")
            quote = request.form.get("quote")
            email = session["email"]
            if name and quote and email:
                update_name_quote(name, quote, email)
                user_data = get_all_user_data()
                return render_template("index.html", user_data = user_data)
        user_data = get_all_user_data()
        return render_template("index.html", user_data = user_data)
    else:
        return redirect(url_for('login'))
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2225, debug=True)
