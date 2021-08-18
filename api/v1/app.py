#!/usr/bin/python3
"""
Api for Find My Face
"""

from os import name
import json
import base64
from werkzeug.utils import secure_filename
from models import storage
from models.known import Known
from models.unknown import Unknown
from testings.test import testMethod
from flask import Flask, render_template, redirect, request, url_for, jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/respuesta", methods=['POST'])
def respuesta():
    res = request.json

    base64_img_bytes = res['source'].encode('utf-8')
    with open('api/v1/static/images/known/test.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

        testMethod('api/v1/static/images/known/test.png', 'api/v1/static/images/known/test.png')

    return jsonify(res)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
