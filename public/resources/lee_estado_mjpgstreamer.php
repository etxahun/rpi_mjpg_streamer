<?php

// Configuration file: contains project path
include('project_path_config.php');

$file = fopen("$rpi_mjpg_streamer_path/public/resources/estado_mjpgstreamer.txt", "r") or die("Unable to open estado_mjpgstreamer.txt file!");
echo fgetc($file);
fclose($file);
?>
