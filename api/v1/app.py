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

    image_one = 'api/v1/static/images/known/{}'.format(res['nombre_uno'])
    image_two = 'api/v1/static/images/unknown/{}'.format(res['nombre_dos'])

    base64_imgOne_bytes = res['source_uno'].encode('utf-8')
    with open(image_one, 'wb') as fileOne_to_save:
        decoded_imageOne_data = base64.decodebytes(base64_imgOne_bytes)
        fileOne_to_save.write(decoded_imageOne_data)

    base64_imgTwo_bytes = res['source_dos'].encode('utf-8')
    with open(image_two, 'wb') as fileTwo_to_save:
        decoded_imageTwo_data = base64.decodebytes(base64_imgTwo_bytes)
        fileTwo_to_save.write(decoded_imageTwo_data)

    identify(image_one, res['name_uno'], image_two)

    identified_image = 'api/v1/static/image/identified/Image_testing.jpg'

    with open(identified_image, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

    return jsonify(base64_message)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
