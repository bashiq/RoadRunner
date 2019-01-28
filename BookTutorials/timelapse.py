import os
import time
from picamera import PiCamera

#choose delay time in seconds 
delay =12
camera = PiCamera()
#camera.start_preview()

#below are default locations to put the files and the name to use
directory ="/home/pi/RoadRunner/imgs"
#webfile = directory + filename + stem
# and this is command to run
mycommand = "raspistill -o /home/pi/RoadRunner/imgs/foo.jpg"
#this is the actual 'do stuff' part. It runs forever
while True:
#	camera.start_preview() #keep commented. will show screen but no way of exit without turning off pi
	camera.capture('/home/pi/RoadRunner/foo.jpg')
	#os.system(mycommand)
	print('captured')
	time.sleep(delay)

