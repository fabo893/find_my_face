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
    json_parse = json.dumps(test1)
    return redirect('test.html', test=json_parse)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
