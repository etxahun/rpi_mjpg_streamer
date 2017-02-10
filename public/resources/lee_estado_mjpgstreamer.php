<?php
$file = fopen("/home/pi/rpi_mjpg_streamer/public/resources/estado_mjpgstreamer.txt", "r") or die("Unable to open estado_mjpgstreamer.txt file!");
echo fgetc($file);
fclose($file);
?>
