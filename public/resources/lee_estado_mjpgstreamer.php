<?php
$file = fopen("/root/odamae/odamaeweb_mjpg-streamer/public/resources/estado_mjpgstreamer.txt", "r") or die("Unable to open estado_mjpgstreamer.txt file!");
echo fgetc($file);
fclose($file);
?>
