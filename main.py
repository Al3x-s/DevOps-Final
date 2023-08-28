#!/usr/bin/env python3
from flask import Flask
from flask import requests
from flask import render_template
from flask import redirect
app = Flask(__name__)

@app.route("/")
def login():
    return "<p>Hello Team</p>"
#dp
@app.route("/input", methods=["POST"])
def user_input():
#creating section for user input
    if request.form("Full Name"):
        name = request.form("Full Name")
        print(name)
if __name__ == __main__
    app.run(host="0.0.0.0", port=2225, debug=True)
    
#dp
