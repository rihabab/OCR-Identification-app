import face_recognition
import cv2
import numpy as np
import os
import pickle

def testing(image_path):
    # Load known face encodings and names
    try:
        with open('C:/Users/Rihab/PycharmProjects/pythonProject/pythonProject/base/data/names.pkl', 'rb') as w:
            known_face_names = pickle.load(w)
        with open('C:/Users/Rihab/PycharmProjects/pythonProject/pythonProject/base/data/faces_encodings.pkl', 'rb') as f:
            known_face_encodings = pickle.load(f)
    except:
        print("Error loading previous data or data not found. Please prepare your training data.")

    # Prompt the user for the image path
    
    unknown_image = face_recognition.load_image_file(image_path)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)

    # Assuming one face for simplicity, but you can loop over each face if there are multiple
    try:
        if len(unknown_face_encodings) > 0:
            unknown_face_encoding = unknown_face_encodings[0]

            # Find the closest match among known faces
            matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            print(f"Detected face is: {name}")
            return name
        
    except :
        print("No faces found in the image!")
        return False
    
