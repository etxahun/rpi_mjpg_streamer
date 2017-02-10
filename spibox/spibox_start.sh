#!/bin/bash

# Guardar el estado:
echo -n 1 > "/home/pi/rpi_mjpg_streamer/public/resources/estado_spibox.txt"

# Start SPiBox
cd /home/pi/rpi_mjpg_streamer/spibox
#python spiboxmessenger.py&
python spibox.py&
