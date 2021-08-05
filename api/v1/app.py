#!/usr/bin/python3
"""
Api for Find My Face
"""

from os import name
import json
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
    test1 = request.get_json()

    print(type(test1))

    with open(test1.image, 'rb') as file1:
        binary1 = file1.read()

    Known(name=test1['name'], image=binary1)

    return jsonify({'status': 'ok'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
