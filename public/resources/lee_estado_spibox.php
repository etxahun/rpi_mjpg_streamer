<?php
$file = fopen("/home/pi/rpi_mjpg_streamer/public/resources/estado_spibox.txt", "r") or die("Unable to open estado_spibox.txt file!");
echo fgetc($file);
fclose($file);
?>
