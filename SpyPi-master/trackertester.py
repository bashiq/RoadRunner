import os
from picamera import PiCamera
import shutil
import time
import cv2
import sys
import numpy
import time
import pickle
from imutils.video import VideoStream
import imutils


#-----------------------------------------------------------------------
#------------------FUNCTIONS--------------------------------------------
#-----------------------------------------------------------------------
		
#function will find the last image taken and extract counter number
def fileNamer():
	initialList = os.listdir(directory)
	fList =[x.split('.')[0] for x in initialList]
	if len(fList) != 0:
		print (fList)
		highestcount =int(fList[0].split('_')[1])

	for x in fList:
		#print(max + "<"+ x.split("_")[1])
		if(highestcount < int(x.split('_')[1])):
			highestcount =int(x.split('_')[1])
#_______________________________________________________________________



#put boxes around detected object and save image
def detect_face(face_recog):
	global highestcount

	# Capture frame-by-frame
	frame = vs.read()
	originalframeSize = frame
	frame = imutils.resize(frame, width=200)#by makingframe smaller we allow faster processing


	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		#flags=cv2.cv.CV_HAAR_SCALE_IMAGE#for opencv 3....
		flags = cv2.CASCADE_SCALE_IMAGE
	)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		# also can put a trigger here
		highestcount +=1
		myfile = directory + filename + "_"+ str(highestcount) + stem
		cv2.imwrite(myfile, originalframeSize)
		print('captured ' + str(highestcount))


	# Display the resulting frame
	cv2.imshow('Video', frame)

#_______________________________________________________________________


#--------------------------------------------------------------------
#-------Initializing-------------------------------------------------
#--------------------------------------------------------------------
#choose delay time in seconds 
#delay =10

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
#face_recog = cv2.createLBPHFaceRecognizer()#for opencv 3..
face_recog = faceCascade.cv2.LBPHFaceRecognizer_create()
#video_capture = cv2.VideoCapture(0)



# default location to store files & name to use
directory='/home/pi/RoadRunner/web/imgs/'
filename ="road"
stem =".jpg"
highestcount =0
initialList ={}	

fileNamer()
#print("iam max " + str((max)))	

# Set initial frame size.
frameSize = (960, 720)#change this number to change image resolution for saving
vs = VideoStream(src=0, usePiCamera=True, resolution=frameSize,framerate=32).start()

# Allow the camera to warm up.
time.sleep(1.0)




#this is the actual 'do stuff' part. It runs forever
while True:	

	#do the below function
	detect_face(face_recog)

	checkme = cv2.waitKey(25)

	if checkme & 0xFF == ord('q'):
		print ("Exiting")
		break

	#time.sleep(1) # put a pause in

	#time.sleep(delay)

# When everything is done, release the capture
vs.stop()
cv2.destroyAllWindows()

