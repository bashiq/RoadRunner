#spy-pi 2
#takes image ever 2 minutes
#most current image becomes availible
import os
from picamera import PiCamera
import shutil
import time


camera = PiCamera()

#choose delay time in seconds 
delay =10


# default location to store files & name to use
directory='/home/pi/RoadRunner/web/imgs/'
filename ="road"
stem =".jpg"
highestcount =0
initialList =os.listdir(directory)
fList =[x.split('.')[0] for x in initialList]
if len(fList) != 0:
	print (fList)
	highestcount =int(fList[0].split('_')[1])

	for x in fList:
		#print(max + "<"+ x.split("_")[1])
		if(highestcount < int(x.split('_')[1])):
			highestcount =int(x.split('_')[1])
		
#print("iam max " + str((max)))		
			

#this is the actual 'do stuff' part. It runs forever
while True:	
	highestcount +=1
	myfile = directory + filename + "_"+ str(highestcount) + stem

	#command to run capture
	#camera.start_preview()
	camera.capture(myfile)
	#copy new file to the webfile location so it is web-visible
	#shutil.copy(myfile,webfile)
	print('captured')
	
	
	time.sleep(delay)
		
		
		
