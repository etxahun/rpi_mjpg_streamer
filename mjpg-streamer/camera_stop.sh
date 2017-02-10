#!/bin/bash

if pgrep mjpg_streamer
then
  # Guardar el estado:
  echo -n 0 > "/home/pi_mjpg_streamer/public/resources/estado_mjpgstreamer.txt"

  kill $(pgrep mjpg_streamer) > /dev/null 2>&1
  echo "mjpg_streamer stopped"
else
  echo "mjpg_streamer not running"
fi

