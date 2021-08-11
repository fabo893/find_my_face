#!/usr/bin/python3
"""
Api for Find My Face
"""

from os import name
import json

from werkzeug.utils import secure_filename
from models import storage
from models.known import Known
from models.unknown import Unknown
from flask import Flask, render_template, redirect, request, url_for, jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/display/<dic>")
def display(dic):
    return render_template("test.html", dic=dic)

@app.route("/upload", methods=['POST'])
def upload():
    img = request.files['image_uploads1']

    if not img:
        return 'No img upload', 400

    name = secure_filename(img.filename)
    type = img.mimetype
    binary = img.read()

    known = Known(name=name, type=type)
    known.save()

    """
    if name is not None and tipo is not None:
        js = {'name': name, 'type': tipo}
    else:
        js = {'name': None, 'type': None}

    print(js)
    """
    return "Let's go", 200
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
