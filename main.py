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
@app.route("/input")
def user_input():

#dp
