#!/usr/bin/python3
"""
Api for Find My Face
"""

from os import name
import json
from werkzeug.utils import redirect
from models.known import Known
from models.unknown import Unknown
from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        test1 = request.get_json()
        json_parse = json.dumps(test1)
        return redirect(url_for('display', dic = json_parse))

@app.route('/display/<dic>')
def display(dic):
    return render_template('test.htlm', dic=dic)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
