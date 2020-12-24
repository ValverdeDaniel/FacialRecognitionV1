# Use OpenCV to:
#   1. Access Webcam
#   2. Detect Faces -> in video stream
#   3. Record faces and frames to disk
#

import numpy as np
import argparse
import os
import imutils
import cv2

########################################################################################################################
# GLOBAL VARIABLES

# download haar cascade for facial recognition
# openCV uses the cascade method to do facial recognition "on the fly"
# xml files are required
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

#name of file and number of frames we want to record
numOfPhotos = 20
name = 'Emma'
########################################################################################################################

# This function uses a webcam to start video, detect face, and capture frames where a face was detected
# alternatively, we could pass in a video (assuming the user wanted to submit a short video clip of their pet) and
# parse through the video collecting images in a similar fashion
# NOTES:
#   need to add in functionality/test with a video taken from iphone or other recorder

def captureFrames():
    faceCascade = cv2.CascadeClassifier(haar_model)

    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    i = 0
    while i <= numOfPhotos:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

        # Draw a rectangle around the faces
        # Capture the frame
        for (x, y, w, h) in faces:
            cv2.imwrite(name +str(i)+'.jpg',frame)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)
        i+=1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()




captureFrames()
