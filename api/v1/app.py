#!/usr/bin/python3
"""
Api for Find My Face
"""

from models.known import Known
from flask import Flask, render_template, request, url_for, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload1", methods=["POST"])
def upload_one():
    img1 = request.form.get('image_uploads1')
    Known(img1, name=img1.name)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
