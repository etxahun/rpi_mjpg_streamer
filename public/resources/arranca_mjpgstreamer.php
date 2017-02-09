<?php
//shell_exec("sudo sh /home/pi/01-arrancar_raspistill_y_mjpgstreamer.sh");
$file = fopen("/root/odamae/odamaeweb_mjpg-streamer/public/resources/estado_mjpgstreamer.txt", "w") or die("Unable to open file!");
fwrite($file, "1");
fclose($file);
?>
