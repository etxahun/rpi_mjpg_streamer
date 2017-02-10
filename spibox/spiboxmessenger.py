#!/bin/sh
# spiboxmessenger.py
# look for files in the capture directory then process them
import os
import subprocess
import ConfigParser
import time

class spiboxMessenger:

    def init(self):
        spiboxConf = ConfigParser.ConfigParser()
        spiboxConf.read('/home/pi/rpi_mjpg_streamer/spibox/spibox.conf')
        self.emailsubject = spiboxConf.get('email','emailsubject')
        self.emailrecipient = spiboxConf.get('email','emailrecipient')
        self.emailon = spiboxConf.get('email','on')

    def getFileList(self):
       self.filelist = []
       i = 0
       for file in os.listdir("/home/pi/rpi_mjpg_streamer/resources/photos"):
          if file.endswith(".jpg"):
             self.filelist.extend([None])
             self.filelist[i] = file
             i = i+1

    def moveFiles(self):
        for filename in self.filelist:
            #print('moving'+filename)
            pid = subprocess.call(['sudo','mv','/home/pi/rpi_mjpg_streamer/resources/photos/'+filename,'/home/pi/rpi_mjpg_streamer/resources/archive/'])

    def emailFiles(self):
        print(len(self.filelist))
        for filename in self.filelist:
            #print('emailing'+filename)
            cmd = 'mpack -s "'+self.emailsubject+'" -c image/jpeg /home/pi/rpi_mjpg_streamer/resources/photos/'+filename + ' '+self.emailrecipient
            pid = subprocess.call(cmd, shell=True)


messenger = spiboxMessenger()
while True:
   time.sleep(10)
   messenger.init()
   messenger.getFileList()
   if messenger.emailon == "YES":
      messenger.emailFiles()
   messenger.moveFiles()
