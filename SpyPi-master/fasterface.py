import cv2
import sys
import numpy
import time
import pickle

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
face_recog = cv2.createLBPHFaceRecognizer()
video_capture = cv2.VideoCapture(0)
#video_capture = cv2.VideoCapture("/home/pi/SpyPi-master/me.mp4") # if you want run on video
all_faces = []  # list to store 'known' faces in
face_count = 0
savefile = 'webfaces.dat'


def detect_face(video_capture, all_faces, face_recog, face_count):
    
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #ret = video_capture.set(3, 320)
    #ret = video_capture.set(4,240)

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



    # Display the resulting frame
    cv2.imshow('Video', frame)


while True:#(video_capture.isOpened()):
	
	detect_face(video_capture, all_faces, face_recog, face_count)

	checkme = cv2.waitKey(50)

	if checkme & 0xFF == ord('q'):
		print "Exiting"
		break

	if checkme & 0xFF == ord('s') and len(faces_found) > 0:
		# assumes we are storing one and only one face
		print "Storing a new face"
		face_count = face_count + 1
		all_faces.append(faces_found[0])
		labels = range(face_count)
		face_recog.train(all_faces,numpy.array(labels))

	#time.sleep(1) # put a pause in


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

# also save any 'trained' faces
outfile = open(savefile,'wb')
pickle.dump(all_faces, outfile)
outfile.close()

