import sqlite3
import subprocess
import io
import chardet
import os
import tempfile
import base64
from PIL import Image
from face_det import face_match

# Establish a connection to the SQLite database


def call_face_detect():
    os.system('python face_det/face_detect.py')


def call_face_match(card_number='123456789'):
    conn = sqlite3.connect('pin.sqlite')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SQL query to fetch the blob files
    # cursor.execute('SELECT image FROM aadhaar')
    # Retrieve all the results
    # results = cursor.fetchall()
    cursor.execute('SELECT aadhaar_number FROM map WHERE card_number = ?', (card_number,))
    a_temp = cursor.fetchone()
    print("Hi",a_temp)
    
    cursor.execute('SELECT image FROM aadhaar WHERE aadhaar_number = ?',(a_temp[0],))

    # cursor.execute('SELECT image FROM aadhaar where aadhaar_number=(select aadhaar_number from map where card_number={card_number})')
    db_img=cursor.fetchone()
    print(db_img)
    # # print(db_img)
    # if len(db_img) > 0:
    #     image = db_img[0][0]
    #     print("fetched")
    #     # return True
    #     # Process the image data as needed
    # else:
    #     # Handle the case when no image is found for the given card_number
    #     print("No image found for the card number.")
    #     # return False


    # image = db_img[0][0]
    # binary_data = base64.b64decode(image)
    # image = Image.open(io.BytesIO(binary_data))
    # image.show()




    # string_results = [result[0].decode('latin-1').replace('\x00', '') for result in results]
    # with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    #     temp_file.write('\n'.join(string_results).encode())

    captured_image_path = "C:\\Users\\ankit\\OneDrive\\Documents\\projects\\atm as evm\\img.jpg"
    return face_match.match_faces(captured_image_path,db_img[0])
    
    # command = ['python', 'face_det/face_match.py', db_img]
    # subprocess.run(command)

# os.remove(temp_file.name)
# command = ["python", "face_det/face_match.py"] + string_results
# subprocess.run(command)


# Close the cursor and the database connection
    cursor.close()
    conn.close()
# call_face_match()
