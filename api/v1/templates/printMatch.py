#!/usr/bin/python3
import json
import face_recognition
import sys

known_image = face_recognition.load_image_file(sys.argv[1])
unknown_image = face_recognition.load_image_file(sys.argv[2])

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print('Yes!!!')
else:
    print('No!!!')
