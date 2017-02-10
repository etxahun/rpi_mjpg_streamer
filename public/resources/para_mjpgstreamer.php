<?php
//shell_exec("sudo sh /home/pi/02-parar_raspistill_y_mjpgstreamer.sh");
$file = fopen("/home/pi/rpi_mjpg_streamer/public/resources/estado_mjpgstreamer.txt", "w") or die("Unable to open file!");
fwrite($file, "0");
fclose($file);
?>
