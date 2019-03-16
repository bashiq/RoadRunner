import os
import cv2
import sys
import numpy
import time
import pickle
from imutils.video import VideoStream 
import imutils

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
face_recog = cv2.face.LBPHFaceRecognizer_create()
all_faces=[]
face_count=0
#video_capture = cv2.VideoCapture(0)

# Set initial frame size.
frameSize = (320, 240)
vs = VideoStream(src=0, usePiCamera=True, resolution=frameSize,framerate=30).start()


# Allow the camera to warm up.
time.sleep(1.0)
start = time.time()

def monitor_thermals():
	temp = os.system("vcgencmd measure_temp")
	if (temp>40):
		print(type(temp))

def detect_face(all_faces, face_recog, face_count):
	
	faces_found = []
    	# Capture frame-by-frame
	frame = vs.read()
	frame = imutils.resize(frame, width=200)
	#by makingframe smaller we allow faster processing
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_count+=1
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
	)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		# also can put a trigger here
		cv2.imwrite('/home/pi/RoadRunner/SpyPi-master/me' +str(face_count) + '.png', frame)

		#extract the face as its own image
		#thisface = frame[y:y+w, x:x+h]
		#grayface = cv2.cvColor(thisface, cv2.COLOR_BGR2GRAY)
		#faces_found.append(grayface)


	# Display the resulting frame
	cv2.imshow('Video', frame)
	#return faces_found

	#monitor_thermals()

while True:

	#while (video_capture.isOpened()):
	detect_face(all_faces, face_recog, face_count)
	checkme = cv2.waitKey(25)
	if checkme & 0xFF == ord('q'):
		print("Exiting")
		break
	#time.sleep(1) # put a pause in

# When everything is done, release the capture
cv2.destroyAllWindows()
vs.stop()


