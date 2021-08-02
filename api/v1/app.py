#!/usr/bin/python3
"""
Api for Find My Face
"""

from os import name
import json
from werkzeug.utils import redirect
from models.known import Known
from models.unknown import Unknown
from flask import Flask, render_template, request, url_for, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    test1 = request.get_json()
    print(test1)
    json_parse = json.loads(test1)
    print(json_parse)
    return render_template('test.html')
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
