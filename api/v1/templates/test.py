#!/usr/bin/python3

import requests
import json

def comparar(objs):
    object = requests.post(objs)

    imagen = object.json()

    img = json.dump(imagen)

    return img, 200