#!/usr/bin/python3
"""
Api for Find My Face
"""

from os import name
from werkzeug.utils import redirect
from models.known import Known
from models.unknown import Unknown
from flask import Flask, render_template, request, url_for, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    img1 = request.form.get('image_uploads1')
    with open(img1, 'rb') as f:
        binary = f.read()

    img_one = Known(img1, name="known_img", image=binary)
    img_one.save()

    img2 = request.form.get('image_uploads2')
    with open(img2, 'rb') as f2:
        binary2 = f2.read()

    img_two = Unknown(img2, name="unknown_img", image=binary2)
    img_two.save()

    return redirect("/")
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
