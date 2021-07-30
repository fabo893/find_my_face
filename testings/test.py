#!/usr/bin/python3
import face_recognition

known = face_recognition.load_image_file("images/known/obama.jpg")
unknown = face_recognition.load_image_file("images/unknown/obama_test.jpg")

encoding_known = face_recognition.face_encodings(known)[0]
encoding_unknown = face_recognition.face_encodings(unknown)

face_locations = face_recognition.face_locations(unknown)

print(encoding_unknown)

for face in encoding_unknown:
  result = face_recognition.compare_faces(face, encoding_known)
  if result == True:
    print("FOUNDED")
  else:
    print("NOT FOUND")
