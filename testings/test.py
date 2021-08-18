#!/usr/bin/python3
import face_recognition

def testMethod(img_one, img_two):
  known = face_recognition.load_image_file(img_one)
  unknown = face_recognition.load_image_file(img_two)

  encoding_known = face_recognition.face_encodings(known)[0]
  encoding_unknown = face_recognition.face_encodings(unknown)[0]

  results = face_recognition.compare_faces([encoding_known], encoding_unknown)

  if results[0]:
    print("FOUNDED")
  else:
    print("NOT FOUND")
