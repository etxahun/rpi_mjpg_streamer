import time
import datetime
import subprocess
import os
import RPi.GPIO as GPIO

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

PIR = 4
def photo():
    for i in range(1,2):
        capturename = get_file_name()
        print('Motion detected! Taking snapshot')
        cmd="raspistill -w 640 -h 480 -rot 270 -n -t 10 -q 10 -e jpg -th none -o /home/pi/rpi_mjpg_streamer/resources/photos/" + capturename+"_%d.jpg" % (i)
        #cmd="raspistill -rot 270 -o /home/odamae/spibox/capture/" + capturename+"_%d.jpg" % (i)
        camerapid = subprocess.call(cmd,shell=True)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)

try:
    print "Turning on motion sensor..."
 
    # Loop until PIR indicates nothing is happening
    while GPIO.input(PIR)==1:
        Current_State  = 0
 
    print "  Sensor ready"
 
    while True:
        print('Waiting for movement')
        GPIO.wait_for_edge(PIR,GPIO.RISING)
        photo()

except KeyboardInterrupt:
  print "  Bye for now"
  # Reset GPIO
  GPIO.cleanup()

