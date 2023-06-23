import face_recognition
import cv2
import numpy as np
import sys,os

# # captured_image = face_recognition.load_image_file("C:\\Users\\ankit\\OneDrive\\Documents\\projects\\atm as evm\\img.jpg")
# captured_image = face_recognition.load_image_file("img.jpg")
# captured_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)

# # Assuming you have a list of image file paths in your database
# database_file = sys.argv[1]
# file_path=os.path.abspath(database_file)
# with open(file_path, 'r' , encoding='utf-8') as file:
#     database_images = file.read()
# # Create an empty list to store the encoded representations of the database images
# database_encodings = []

# # Loop through each image in the database
# for image_path in database_images:
#     database_image = face_recognition.load_image_file(image_path)
#     database_image_encoding = face_recognition.face_encodings(database_image)[0]
#     database_encodings.append(database_image_encoding)

# # Encode the captured image
# captured_image_encoding = face_recognition.face_encodings(captured_image)[0]

# # Iterate through the database encodings and compare with the captured image encoding
# for database_encoding in database_encodings:
#     similarity_score = face_recognition.face_distance([database_encoding], captured_image_encoding)
#     if similarity_score < 0.6:  # Adjust the threshold as needed
#         print("Match found!")
#         # Perform further actions for a match
#         break

#     if similarity_score >= 0.6:
#         print("No")

# import cv2
# import face_recognition

def match_faces(captured_image_path, database_image_path,c):
    c+=1
    # Load the captured image and convert it to RGB
    captured_image = face_recognition.load_image_file(captured_image_path)
    captured_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)

    # Load the image from the database and convert it to RGB
    database_image = face_recognition.load_image_file(database_image_path)
    database_image = cv2.cvtColor(database_image, cv2.COLOR_BGR2RGB)

    # Detect faces in the captured image
    captured_face_locations = face_recognition.face_locations(captured_image)
    
    # Extract face encodings from the captured image
    captured_face_encodings = face_recognition.face_encodings(captured_image, captured_face_locations)

    # Detect faces in the database image
    database_face_locations = face_recognition.face_locations(database_image)
    
    # Extract face encodings from the database image
    database_face_encodings = face_recognition.face_encodings(database_image, database_face_locations)

    # Compare the captured face encodings with the database face encodings
    for captured_encoding in captured_face_encodings:
        # Compare the captured face encoding with each face encoding in the database
        matches = face_recognition.compare_faces(database_face_encodings, captured_encoding)

        # Check if any match is found
        if any(matches):
            return True,c
        else:
            return False,c

# Path to the captured image and the database image
# captured_image_path = 'C:\\Users\\ankit\OneDrive\\Pictures\\Camera Roll\\ankitha.jpg'
# database_image_path = 'C:\\Users\\ankit\OneDrive\\Pictures\\Camera Roll\\anni.jpg'

# # Perform face matching
# match_faces(captured_image_path, database_image_path)

# # import face_recognition
# # import cv2
# # import numpy as np

# # captured_image = face_recognition.load_image_file('C:\\Users\\ankit\\OneDrive\\Documents\\projects\\atm as evm\\img.jpg')
# # captured_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
# # # Assuming you have a list of image file paths in your database

# # database_images = ["image1.jpg", "image2.jpg", "image3.jpg"]

# # # Create an empty list to store the encoded representations of the database images
# # database_encodings = []

# # # Loop through each image in the database
# # for image_path in database_images:
# #     database_image = face_recognition.load_image_file(image_path)
# #     database_image_encoding = face_recognition.face_encodings(database_image)[0]
# #     database_encodings.append(database_image_encoding)
# # # Encode the captured image
# # captured_image_encoding = face_recognition.face_encodings(captured_image)[0]

# # # Iterate through the database encodings and compare with the captured image encoding
# # for database_encoding in database_encodings:
# #     similarity_score = face_recognition.face_distance([database_encoding], captured_image_encoding)
# #     if similarity_score < 0.6:  # Adjust the threshold as needed
# #         print("Match found!")
# #         # Perform further actions for a match
# #         break
