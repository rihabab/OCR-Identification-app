import os
import pickle
import face_recognition

def processing():
    known_faces_dir = 'known_faces'
    known_face_encodings = []
    known_face_names = []

    # Iterate over each image in the known_faces directory
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(image_path)
            
            # Extract face encodings from the image
            encodings = face_recognition.face_encodings(image)
            
            if len(encodings) > 0:  # if a face is detected
                known_face_encodings.append(encodings[0])
                known_face_names.append(filename.split('.')[0])  # Assuming filename is "Name.jpg"

    # Save the data to pickle files
    if not os.path.exists('data'):
        os.makedirs('data')

    with open('data/names.pkl', 'wb') as w:
        pickle.dump(known_face_names, w)
    with open('data/faces_encodings.pkl', 'wb') as f:
        pickle.dump(known_face_encodings, f)

    print("Data prepared and saved!")