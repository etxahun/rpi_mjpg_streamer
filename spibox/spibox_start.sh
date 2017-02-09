#!/bin/bash

# Guardar el estado:
echo -n 1 > "/root/odamae/odamaeweb_mjpg-streamer/public/resources/estado_spibox.txt"

# Start SPiBox
cd /home/odamae/odamaeweb_mjpg-streamer/spibox
#python spiboxmessenger.py&
python spibox.py&
