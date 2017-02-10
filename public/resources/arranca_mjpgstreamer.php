<?php
$file = fopen("/home/pi/rpi_mjpg_streamer/public/resources/estado_mjpgstreamer.txt", "w") or die("Unable to open file!");
fwrite($file, "1");
fclose($file);
?>
