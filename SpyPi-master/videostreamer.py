import cv2
import sys
import numpy
import time
import pickle
from imutils.video import FileVideoStream
import imutils

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
face_recog = cv2.createLBPHFaceRecognizer()

# Set initial frame size.
frameSize = (320, 240)
fvs = FileVideoStream("/home/pi/RoadRunner/SpyPi-master/me1.avi").start()
# Allow the camera to warm up.
time.sleep(1.0)

def detect_face():
    
    # Capture frame-by-frame
    frame = fvs.read()
    frame = imutils.resize(frame, width=120)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	# also can put a trigger here
	#cv2.imwrite('/home/pi/RoadRunner/SpyPi-master/me1.png', frame)
	print('capturing frame')


    # Display the resulting frame
    
    cv2.imshow('Video', frame)

while fvs.more():
	
	detect_face()

	checkme = cv2.waitKey(50)

	if checkme & 0xFF == ord('q'):
		print "Exiting"
		break

# When everything is done, release the capture
cv2.destroyAllWindows()
fvs.stop()
