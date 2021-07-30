#!/usr/bin/python3
"""
Api for Find My Face
"""

import models
from models.known import Known
from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/find", methods=["POST"])
def save():
    return {{ url_for('identify.py, img1, img2') }}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5002', debug=True)
