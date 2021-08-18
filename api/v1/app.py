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
from testings.TestIdentify import identify
from flask import Flask, render_template, redirect, request, url_for, jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/respuesta", methods=['POST'])
def respuesta():
    res = request.json

    image_one = 'api/v1/static/images/known/{}'.format(res['nombre'])
    image_two = 'api/v1/static/images/known/{}'.format(res['nombre'])

    base64_img_bytes = res['source'].encode('utf-8')
    with open(image_one, 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

        identify(image_one, "Fabian", image_two)

    return jsonify(res)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
