<?php

// Configuration file: contains project path
include('project_path_config.php');

$file = fopen("$rpi_mjpg_streamer_path/public/resources/estado_mjpgstreamer.txt", "w") or die("Unable to open file!");
fwrite($file, "0");
fclose($file);
?>
