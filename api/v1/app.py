#!/usr/bin/python3
"""
Api for Find My Face
"""

from os import name
import json
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
    img = request.get_json()
    print(img)
    test = {'prueba': 'ok'}
    return jsonify(test)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
