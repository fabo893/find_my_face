#!/usr/bin/python3
"""
Api for Find My Face
"""
import models
from models.known import Known
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    img1 = request.form.get("img_uploads1")
    Known(img1)
    return "Yes"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5002', debug=True)
