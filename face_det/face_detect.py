import cv2
from ecapture import ecapture as ec

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(0)

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # apply the function created to the video frame

    cv2.imshow(
        "Face Detection", video_frame
    )  # display the processed frame in a window named "Face Detection"
    ec.capture(0, "Jarvis Camera ", "img.jpg")
    break

    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break

video_capture.release()
