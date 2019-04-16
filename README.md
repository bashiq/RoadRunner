# RoadRunner
repo for source code

### Installation instructions for RoadRunner Application

Obtain a Raspberry Pi 3 Model B+ and a Raspberry Pi camera v2 module.

On the Pi download the following packages: 
```
fswebcam
feh
python-picamera
python3-picamera
python3
apache2
imagemagick
iotion
python-opencv
numpy
opencv3.4
```
Download the following repo on to the Pi: https://github.com/bashiq/RoadRunner 

Run the application by navigating to the directory `RoadRunner/SpyPi-master` and  executing the following command: `python3 fasterface.py`

To run the application in a headless state, you must use crontab.

Once ready you may mount the Pi system inside a car and provide a power source.



### Installation Instructions for Webserver


Follow tutorial(page 18) of Book 'Make: Jumpstarting Raspberry Pi vision machine learning and facial recognition on a single board computer'

To set up the webserver go to the `/websiteSetup` directory

The goal of this is to add our contents of this folder into the web directory so you may add these files to `/var/www/html`

You now have 2 options, you may either follow below or if you know what you are doing proceed ahead

Tutorial:

do the following where you may create a link/shortcut to easily access this folder in the RoadRunner directory

Type the following:
```
ln -s /var/www/html /home/pi/RoadRunner/web 	//after the directory pi, you may choose/create a shortcut path anywhere you like for example we can create a folder in downloads called web "/home/pi/download/web "
sudo chown pi . *
cd web
mv index.html index-orig.html
```
Now paste the contents of this folder into directory `/home/pi/RoadRunner/web`

To access this website goto chrome and type: localhost

If both devices are the same network goto another computer type the pi name or its ip address

Possible issues:

-you need to ensure your web server is running

-you may need to install php
