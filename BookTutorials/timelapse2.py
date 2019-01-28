#spy-pi 2
#takes image ever 2 minutes
#most current image becomes availible
import os
import time
from picamera import PiCamera
import shutil

camera = PiCamera()
#camera.start_preview() 

#choose delay time in seconds 
delay =5
#says to save 7 days (1 week) at a time
savedays=7
#book says do not change this code, converts our savedays to how often to retake
#a pic in secs
#note that 1 day at 1 pic/min is 10,080 files per week
waitcount = savedays * 24*60*60 / delay

# default location to store files & name to use
directory='/home/pi/RoadRunner/web/imgs/'
filename ="spycam"
stem =".jpg"

#this is the file the webserver expects
webfile= directory+filename+stem

#command to run capture
icount =0

#this is the actual 'do stuff' part. It runs forever
while True:	
	icount +=1
	myfile = directory + filename + "_"+ str(icount) + stem
	#camera.start_preview()
	camera.capture(myfile)
	#copy new file to the webfile location so it is web-visible
	shutil.copy(myfile,webfile)
	print('captured')
	
	#new purge roputine removes oldder images after expiration time
	inix = icount - waitcount
	
	if inix > 0:
		deleteme= directory + str(inix)+ filename + stem
		os.remove(deleteme)
	
	time.sleep(delay)
		
		
		
