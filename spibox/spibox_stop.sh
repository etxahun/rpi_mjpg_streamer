#!/bin/bash

#if pgrep python
if (ps aux|grep "[s]piboxmessenger.py" | awk '{ print $2 }')
then
  # Guardar el estado:
  echo -n 0 > "/root/odamae/odamaeweb_mjpg-streamer/public/resources/estado_spibox.txt"

  #kill $(pgrep python) > /dev/null 2>&1
  #kill $(ps aux|grep "[s]piboxmessenger.py" | awk '{ print $2 }')
  kill $(ps aux|grep "[s]pibox.py" | awk '{ print $2 }')
  echo "spibox stopped"
else
  echo "spibox not running"
fi

