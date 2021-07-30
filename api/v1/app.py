#!/usr/bin/python3
"""
Api for Find My Face
"""
from flask import Flask, jsonify
from models import storage

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(exception=None):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run('0.0.0.0', '5000', threaded=True)