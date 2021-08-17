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

@app.route("/respuesta", methods=['POST'])
def respuesta():
    res = request.json

    with open(res['dataURL'], 'rb') as file:
        binary = file.read()
        print(binary)

    '''print(res['nombre'])'''
    return jsonify(res)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
